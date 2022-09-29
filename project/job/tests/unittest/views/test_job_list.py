from django.test import TestCase
from model_bakery import baker

from project.job.facade import get_activated_authorized_job_list
from project.job.views import JobList


class JobListUnittest(TestCase):
    def test_job_list_get_queryset(self):
        baker.make('Job', status=False, checked=True)
        baker.make('Job', status=True, checked=True)

        baker.make('Job', status=False, checked=False)
        baker.make('Job', status=True, checked=False)

        self.assertQuerysetEqual(
            set(get_activated_authorized_job_list()),
            set(JobList().get_queryset()),
        )
