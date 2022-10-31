from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from project.job.models import Application


class JobApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = ['job', 'candidate', 'status', 'score']
