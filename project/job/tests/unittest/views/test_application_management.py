from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.test import TestCase
from model_bakery import baker

from project.job.facade import get_user_application_list
from project.job.views import ApplicationManagement


class ApplicationManagementUnittest(TestCase):
    def test_application_list_get_queryset(self):
        user = baker.make(get_user_model())
        baker.make('Application', candidate=user)
        baker.make('Application')

        view = ApplicationManagement()
        view.request = HttpRequest()
        view.request.user = user

        self.assertQuerysetEqual(
            set(get_user_application_list(user)),
            set(view.get_queryset()),
        )
