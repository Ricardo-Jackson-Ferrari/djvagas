from django.test import TestCase

from project.account.views import AccountCreateView
from project.roles import *


class AccountCreateViewTest(TestCase):
    def setUp(self):
        self.view = AccountCreateView
        self.view.success_url = '/'

    def test_form_valid_candidate_role(self):
        data = {
            'first_name': 'test',
            'email': 'test@email.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'role': Candidate.get_name(),
        }
        form = self.view.form_class(data)

        resp = self.view().form_valid(form)

        self.assertEqual(302, resp.status_code)

    def test_form_valid_company_role(self):
        data = {
            'first_name': 'test',
            'email': 'test@email.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'role': Company.get_name(),
        }
        form = self.view.form_class(data)

        resp = self.view().form_valid(form)

        self.assertEqual(302, resp.status_code)
