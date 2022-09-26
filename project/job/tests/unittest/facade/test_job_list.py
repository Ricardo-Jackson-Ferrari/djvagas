from django.test import TestCase
from model_bakery import baker

from project.job.facade import get_job_list
from project.job.models import Job


class JobListUnittest(TestCase):
    def test_get_job_list_queryset_return(self):
        self.assertQuerysetEqual(
            Job.objects.filter(status=True), get_job_list()
        )

    def test_get_job_list_count_return(self):
        baker.make(Job, status=False)
        baker.make(Job, status=True)
        self.assertEqual(1, get_job_list().count())
