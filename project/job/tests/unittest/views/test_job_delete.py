from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from model_bakery import baker

from project.job import facade
from project.job.views import JobDelete


class JobDeleteUnittest(TestCase):
    def test_delete_list_get_queryset(self):
        baker.make('Job', status=False, checked=True)
        baker.make('Job', status=True, checked=True)

        baker.make('Job', status=False, checked=False)
        baker.make('Job', status=True, checked=False)

        self.assertEqual(
            set(facade.get_full_job_list()),
            set(JobDelete().get_queryset()),
        )

    def test_delete_job_on_owner_status_code_200(self):
        job = baker.make('Job')
        url = reverse_lazy('job:delete', kwargs={'slug': job.slug})
        self.client.force_login(job.company)

        response = self.client.post(url, follow=True)

        self.assertEqual(response.status_code, 200)

    def test_delete_job_on_no_owner_status_code_401(self):
        job = baker.make('Job')
        another_company = baker.make(get_user_model())
        url = reverse_lazy('job:delete', kwargs={'slug': job.slug})
        self.client.force_login(another_company)

        response = self.client.post(url)

        self.assertEqual(response.status_code, 401)
