from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView

from project.job import facade


class JobDetail(DetailView):
    template_name = 'job/job_detail.html'
    extra_context = {'tittle': _('job detail')}
    queryset = facade.get_authorized_job_list()
