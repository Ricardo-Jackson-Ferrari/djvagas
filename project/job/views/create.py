from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from project.job.forms import JobCreateForm


class JobCreate(CreateView):
    template_name = 'job/job_form.html'
    form_class = JobCreateForm
    extra_context = {'tittle': _('job registration')}
