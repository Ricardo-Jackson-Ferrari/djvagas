from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from project.job.mixins import FormMixin
from project.job.models import Job


class JobCreateForm(FormMixin, ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_attr_placeholder('title', _('job title'))

    class Meta:
        model = Job
        exclude = ('company',)
