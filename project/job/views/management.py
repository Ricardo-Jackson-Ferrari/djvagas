from django.views.generic import ListView

from project.job import facade


class JobManagement(ListView):
    template_name = 'job/job_management.html'

    def get_queryset(self):
        return facade.get_user_job_list(user=self.request.user)
