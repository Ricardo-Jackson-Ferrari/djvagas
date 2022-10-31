from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from project.roles import *


class Base(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('created at')
    )
    updated_on = models.DateTimeField(
        auto_now=True, verbose_name=_('updated on')
    )

    class Meta:
        abstract = True


class Schooling(models.Model):
    schooling = models.CharField(
        max_length=30, unique=True, verbose_name=_('schooling')
    )
    level = models.PositiveIntegerField(verbose_name=_('level'))

    def __str__(self) -> str:
        return self.schooling

    def __gt__(self, obj):
        if self.level > obj.level:
            return True
        return False

    def __ge__(self, obj):
        if self.level >= obj.level:
            return True
        return False

    def __eq__(self, obj):
        if self.level == obj.level:
            return True
        return False

    class Meta:
        verbose_name = _('schooling')
        verbose_name_plural = _('schoolings')


class Job(Base):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    status = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, verbose_name=_('friendly url'))
    schooling = models.ForeignKey(
        to=Schooling, on_delete=models.DO_NOTHING, verbose_name=_('schooling')
    )
    salary_from = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0.0)],
        verbose_name=_('salary from'),
    )
    salary_to = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0.0)],
        verbose_name=_('salary to'),
    )
    company = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        limit_choices_to=Q(groups__name=Company.get_name()),
        on_delete=models.CASCADE,
        verbose_name=_('company'),
    )
    description = models.TextField(
        max_length=500, verbose_name=_('description')
    )

    def __str__(self) -> str:
        return self.title

    def clean(self):
        if self.salary_from > self.salary_to:
            raise ValidationError(
                _('"salary to" cannot be less than "salary from"')
            )

    class Meta:
        verbose_name = _('job')


class Application(Base):
    status = models.BooleanField(default=True)
    job = models.ForeignKey(
        to=Job, on_delete=models.CASCADE, verbose_name=_('job')
    )
    candidate = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        limit_choices_to={'groups__name': Candidate.get_name()},
        on_delete=models.CASCADE,
        verbose_name=_('candidate'),
    )
    salary_expectation = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0.0)],
        verbose_name=_('salary expectation'),
    )

    score = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0.0)],
        verbose_name=_('score'),
    )

    def calculate_score(self):
        profile = self.candidate.profilecandidate
        max_score = 100
        max_parity = 2
        candidate_parity = 0

        if profile.schooling is not None:
            if profile.schooling >= self.job.schooling:
                candidate_parity += 1

        if self.job.salary_to >= self.salary_expectation:
            candidate_parity += 1

        score = max_score / max_parity * candidate_parity

        return score

    def save(self, *args, **kwargs):
        self.score = self.calculate_score()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.job.title

    def unique_error_message(self, model_class, unique_check):
        error = super().unique_error_message(model_class, unique_check)

        if model_class == type(self) and unique_check == ('candidate', 'job'):
            error.message = _('%(candidate)s already registered for job.')
            error.params['candidate'] = self.candidate

        return error

    class Meta:
        verbose_name = _('application')
        unique_together = ['candidate', 'job']
