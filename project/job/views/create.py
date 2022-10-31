from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from rolepermissions.mixins import HasRoleMixin

from project.job.forms import JobCreateForm
from project.roles import Company


class JobCreate(HasRoleMixin, CreateView):
    template_name = 'job/job_form.html'
    form_class = JobCreateForm
    extra_context = {'tittle': _('job registration')}
    allowed_roles = Company.get_name()
