from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import NON_FIELD_ERRORS

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

    class Meta:
        verbose_name = _('schooling')
        verbose_name_plural = _('schoolings')


class Salary(models.Model):
    salary_range = models.CharField(
        max_length=30, unique=True, verbose_name=_('salary range')
    )

    def __str__(self) -> str:
        return self.salary_range

    class Meta:
        verbose_name = _('salary')
        verbose_name_plural = _('salaries')


class Job(Base):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    status = models.BooleanField(default=False)
    slug = models.SlugField(verbose_name=_('friendly url'), unique=True)
    schooling = models.ForeignKey(
        to=Schooling, on_delete=models.DO_NOTHING, verbose_name=_('schooling')
    )
    salary_range = models.ForeignKey(
        to=Salary, on_delete=models.DO_NOTHING, verbose_name=_('salary range')
    )
    company = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('company'),
    )
    description = models.TextField(
        max_length=500, verbose_name=_('description')
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('job')


class Application(Base):
    status = models.BooleanField(default=True)
    experience = models.TextField(verbose_name=_('experience'))
    attending = models.BooleanField(default=False, verbose_name=_('attending'))
    objective = models.TextField(verbose_name=_('objective'))
    schooling = models.ForeignKey(
        to=Schooling, on_delete=models.DO_NOTHING, verbose_name=_('schooling')
    )
    job = models.ForeignKey(
        to=Job, on_delete=models.CASCADE, verbose_name=_('job')
    )
    candidate = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('candidate'),
    )
    salary_expectation = models.ForeignKey(
        to=Salary,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('salary expectation'),
    )

    def __str__(self) -> str:
        return self.job.title

    def validate_unique(self, exclude=None) -> None:
        return super().validate_unique(exclude)

    def unique_error_message(self, model_class, unique_check):
        error = super().unique_error_message(model_class, unique_check)

        if model_class == type(self) and unique_check == ('candidate', 'job'):
            error.message = _(f'{self.candidate} already registered for job.')

        return error

    class Meta:
        verbose_name = _('application')
        unique_together = ['candidate', 'job']
