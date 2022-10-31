from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from rolepermissions.mixins import HasRoleMixin

from project.job import facade
from project.roles import Company


class JobDelete(HasRoleMixin, DeleteView):
    success_url = reverse_lazy('job:management')
    queryset = facade.get_full_job_list()
    allowed_roles = Company.get_name()

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.company != self.request.user:
            return HttpResponse('Unauthorized', status=401)
        return super().dispatch(request, *args, **kwargs)
