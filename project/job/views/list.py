from django.views.generic import ListView

from project.job import facade


class JobList(ListView):
    template_name = 'job/job_list.html'

    def get_queryset(self):
        return facade.get_job_list()
