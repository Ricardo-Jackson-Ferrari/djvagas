from django.http import HttpRequest
from django.test import TestCase
from model_bakery import baker
from pytest import mark

from project.job.facade import get_user_application_list
from project.job.views import ApplicationManagement


class ApplicationManagementUnittest(TestCase):
    @mark.usefixtures('user_candidate_cls')
    def test_application_list_get_queryset(self):
        user = self.user_candidate()
        another_user = self.user_candidate()
        baker.make('Application', candidate=user)
        baker.make('Application', candidate=another_user)

        view = ApplicationManagement()
        view.request = HttpRequest()
        view.request.user = user

        self.assertQuerysetEqual(
            set(get_user_application_list(user)),
            set(view.get_queryset()),
        )
