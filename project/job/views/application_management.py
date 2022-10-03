from django.views.generic import ListView

from project.job import facade


class ApplicationManagement(ListView):
    template_name = 'job/application_management.html'

    def get_queryset(self):
        self.queryset = facade.get_user_application_list(
            user=self.request.user
        )
        return super().get_queryset()
