from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView

from project.job import facade


class JobList(ListView):
    template_name = 'job/job_list.html'
    extra_context = {'tittle': _('job list')}
    paginate_by = settings.PER_PAGE

    def get_queryset(self):
        self.queryset = facade.get_activated_authorized_job_list()
        return super().get_queryset()
