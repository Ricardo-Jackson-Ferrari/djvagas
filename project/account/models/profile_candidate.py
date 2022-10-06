from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from project.job.models import Schooling
from project.roles import Candidate


class ProfileCandidate(models.Model):
    candidate = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'groups__name': Candidate.get_name()},
        verbose_name=_('candidate'),
    )
    objective = models.TextField(blank=True, verbose_name=_('objective'))
    schooling = models.ForeignKey(
        to=Schooling,
        on_delete=models.DO_NOTHING,
        blank=True,
        verbose_name=_('schooling'),
    )
    attending = models.BooleanField(default=False, verbose_name=_('attending'))
    experience = models.TextField(blank=True, verbose_name=_('experience'))

    def __str__(self) -> str:
        return self.user.first_name
