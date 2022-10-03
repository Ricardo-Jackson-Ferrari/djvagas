from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker
from pytest import mark

from project.job import facade
from project.job.models import Application, Job


@mark.unit
class JobListUnittest(TestCase):
    def setUp(self) -> None:
        baker.make(Job, status=False, checked=True)
        baker.make(Job, status=True, checked=True)

        baker.make(Job, status=False, checked=False)
        baker.make(Job, status=True, checked=False)

    def test_get_activated_authorized_job_list_queryset_return(self):
        self.assertQuerysetEqual(
            set(Job.objects.filter(status=True, checked=True)),
            set(facade.get_activated_authorized_job_list()),
        )

    def test_get_activated_authorized_job_list_count_return(self):
        self.assertEqual(1, facade.get_activated_authorized_job_list().count())

    def test_get_full_job_list(self):
        self.assertEqual(4, facade.get_full_job_list().count())

    def test_get_user_job_list(self):
        job = baker.make(Job)
        self.assertEqual(1, facade.get_user_job_list(job.company).count())

    def test_get_user_application_list(self):
        user = baker.make(get_user_model())
        baker.make(Application, candidate=user)

        self.assertEqual(1, facade.get_user_application_list(user).count())
