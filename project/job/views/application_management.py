from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from rolepermissions.mixins import HasRoleMixin

from project.job import facade
from project.roles import Candidate


class ApplicationManagement(HasRoleMixin, ListView):
    template_name = 'job/application_management.html'
    allowed_roles = Candidate.get_name()
    extra_context = {'title': _('application management')}

    def get_queryset(self):
        self.queryset = facade.get_user_application_list(
            user=self.request.user
        )
        return super().get_queryset()
