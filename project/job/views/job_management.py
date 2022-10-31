from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from rolepermissions.mixins import HasRoleMixin

from project.job import facade
from project.roles import Company


class JobManagement(HasRoleMixin, ListView):
    template_name = 'job/job_management.html'
    allowed_roles = Company.get_name()
    extra_context = {'title': _('job management')}

    def get_queryset(self):
        self.queryset = facade.get_user_job_list(user=self.request.user)
        return super().get_queryset()
