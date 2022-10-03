from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from project.job import facade


class JobDelete(DeleteView):
    success_url = reverse_lazy('job:management')

    def get_queryset(self):
        self.queryset = facade.get_full_job_list()
        return super().get_queryset()

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.company != self.request.user:
            return HttpResponse('Unauthorized', status=401)
        return super().dispatch(request, *args, **kwargs)
