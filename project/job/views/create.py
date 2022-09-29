from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from project.job import facade


class JobCreate(CreateView):
    template_name = 'job/job_create.html'
    form_class = facade.get_job_create_form()
    extra_context = {'tittle': _('job registration')}
