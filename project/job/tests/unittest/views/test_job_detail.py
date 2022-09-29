from django.test import TestCase
from model_bakery import baker

from project.job.facade import get_full_authorized_job_list
from project.job.views import JobDetail


class JobDetailUnittest(TestCase):
    def test_detail_list_get_queryset(self):
        baker.make('Job', status=False, checked=True)
        baker.make('Job', status=True, checked=True)

        baker.make('Job', status=False, checked=False)
        baker.make('Job', status=True, checked=False)

        self.assertEqual(
            set(get_full_authorized_job_list()),
            set(JobDetail().get_queryset()),
        )
