from django.test import TestCase
from model_bakery import baker
from pytest import mark

from project.job import facade
from project.job.models import Application, Job


class FacadeUnittest(TestCase):
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

    @mark.usefixtures('user_candidate_cls')
    def test_get_user_application_list(self):
        candidate = self.user_candidate()
        baker.make(Application, candidate=candidate)

        self.assertEqual(
            1, facade.get_user_application_list(candidate).count()
        )

    def test_get_job_with_slug(self):
        job = baker.make(Job, status=True, checked=True)
        self.assertEqual(
            job, facade.get_job_activated_authorized_with_slug(job.slug)
        )
