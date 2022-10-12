from django.contrib.auth import get_user_model
from django.http import Http404, HttpRequest
from django.test import TestCase
from django.urls import reverse_lazy
from model_bakery import baker
from rolepermissions.roles import assign_role

from project.job.views import JobApplication
from project.roles import Candidate


class JobApplicationUnittest(TestCase):
    def setUp(self):
        self.job = baker.make('Job', status=True, checked=True)
        self.user = baker.make(get_user_model())
        assign_role(self.user, Candidate.get_name())

    def test_method_get_200_return(self):
        request = HttpRequest()
        request.user = self.user

        request.method = 'GET'

        resp = JobApplication.as_view()(request, slug=self.job.slug)

        self.assertEqual(200, resp.status_code)

    def test_method_get_404_return(self):
        request = HttpRequest()
        request.user = self.user

        request.method = 'GET'

        self.assertRaises(
            Http404,
            JobApplication.as_view(),
            request=request,
            slug=self.job.slug + 'a',
        )

    def test_method_post_404_return(self):
        self.client.force_login(self.user)
        url = reverse_lazy('job:application', kwargs={'slug': self.job.slug})
        resp = self.client.post(
            url[:-1],
            data={'salary_expectation': 1},
        )

        self.assertEqual(404, resp.status_code)

    def test_method_post_302_return(self):
        self.client.force_login(self.user)
        url = reverse_lazy('job:application', kwargs={'slug': self.job.slug})
        resp = self.client.post(
            url,
            data={'salary_expectation': 1},
        )

        self.assertEqual(302, resp.status_code)
