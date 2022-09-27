from django.utils.translation import gettext_lazy as _

from project.job.models import Job

from .base_model_form import BaseModelForm


class JobCreateForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_attr_placeholder('title', _('job title'))

    class Meta:
        model = Job
        exclude = ('company',)
