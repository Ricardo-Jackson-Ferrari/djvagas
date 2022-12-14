from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from project.job import facade
from project.job.forms import JobUpdateForm


class JobUpdate(UpdateView):
    success_url = reverse_lazy('job:management')
    queryset = facade.get_full_job_list()
    form_class = JobUpdateForm
    template_name = 'job/job_form.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.company != self.request.user:
            return HttpResponse('Unauthorized', status=401)
        return super().dispatch(request, *args, **kwargs)
