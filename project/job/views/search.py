from django.conf import settings
from django.db.models import Q
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView

from project.job import facade


class JobSearch(ListView):
    template_name = 'job/job_list.html'
    extra_context = {'title': _('search')}
    paginate_by = settings.PER_PAGE
    ordering = '-created_at'

    def get_queryset(self):
        search_term = self.request.GET.get('q', '').strip()

        if not search_term:
            raise Http404()

        self.queryset = facade.get_activated_authorized_job_list().filter(
            Q(title__icontains=search_term)
            | Q(description__icontains=search_term)
        )

        return super().get_queryset()
