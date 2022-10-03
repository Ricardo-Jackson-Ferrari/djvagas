from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView

from project.job import facade


class JobDetail(DetailView):
    template_name = 'job/job_detail.html'
    extra_context = {'tittle': _('job detail')}

    def get_queryset(self):
        self.queryset = facade.get_full_authorized_job_list()
        return super().get_queryset()
