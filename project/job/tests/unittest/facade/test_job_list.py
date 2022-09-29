from django.test import TestCase
from model_bakery import baker
from pytest import mark

from project.job.facade import get_activated_authorized_job_list
from project.job.models import Job


@mark.unit
class JobListUnittest(TestCase):
    def test_get_job_list_queryset_return(self):
        self.assertQuerysetEqual(
            Job.objects.filter(status=True),
            get_activated_authorized_job_list(),
        )

    def test_get_job_list_count_return(self):
        baker.make(Job, status=False, checked=True)
        baker.make(Job, status=True, checked=True)

        baker.make(Job, status=False, checked=False)
        baker.make(Job, status=True, checked=False)

        self.assertEqual(1, get_activated_authorized_job_list().count())
