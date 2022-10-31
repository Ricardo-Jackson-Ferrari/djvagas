from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from rolepermissions.mixins import HasRoleMixin

from project.job import facade
from project.job.forms import JobApplicationForm
from project.roles import Candidate


class JobApplication(HasRoleMixin, SuccessMessageMixin, CreateView):
    form_class = JobApplicationForm
    template_name = 'job/job_form.html'
    extra_context = {'title': _('job application')}
    success_url = reverse_lazy('job:application_management')
    success_message = _('Enrollment successful')
    allowed_roles = Candidate.get_name()

    def get(self, request, *args, **kwargs):
        try:
            facade.get_job_activated_authorized_with_slug(self.kwargs['slug'])
            return super().get(request, *args, **kwargs)
        except facade.JobDoesNotExist:
            raise Http404()

    def form_valid(self, form):
        try:
            job = facade.get_job_activated_authorized_with_slug(
                self.kwargs['slug']
            )
            form.instance.candidate = self.request.user
            form.instance.job = job
            return super().form_valid(form)
        except facade.JobDoesNotExist:
            raise Http404()
