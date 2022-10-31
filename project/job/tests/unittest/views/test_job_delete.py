from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from model_bakery import baker
from rolepermissions.roles import assign_role

from project.roles import Company


class JobDeleteUnittest(TestCase):
    def setUp(self) -> None:
        self.job = baker.make('Job')
        assign_role(self.job.company, Company)

    def test_delete_job_on_owner_status_code_200(self):
        url = reverse_lazy('job:delete', kwargs={'slug': self.job.slug})
        self.client.force_login(self.job.company)

        response = self.client.post(url, follow=True)

        self.assertEqual(response.status_code, 200)

    def test_delete_job_on_no_owner_status_code_401(self):
        another_company = baker.make(get_user_model())
        url = reverse_lazy('job:delete', kwargs={'slug': self.job.slug})
        self.client.force_login(another_company)

        response = self.client.post(url)

        self.assertEqual(response.status_code, 401)
