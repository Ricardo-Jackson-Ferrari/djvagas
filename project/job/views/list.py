from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView

from project.job import facade


class JobList(ListView):
    template_name = 'job/job_list.html'
    extra_context = {'tittle': _('job list')}

    def get_queryset(self):
        return facade.get_activated_authorized_job_list()
