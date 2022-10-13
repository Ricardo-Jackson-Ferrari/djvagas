from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from project.job.mixins import FormMixin
from project.job.models import Job


class JobUpdateForm(FormMixin, ModelForm):
    class Meta:
        model = Job
        fields = ('status',)
