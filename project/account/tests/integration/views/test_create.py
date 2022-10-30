from django.test import TestCase

from project.account.views import AccountCreateView
from project.roles import *
from rolepermissions.roles import RolesManager
from parameterized import parameterized

class AccountCreateViewTest(TestCase):
    def setUp(self):
        self.view = AccountCreateView
        self.view.success_url = '/'

    @parameterized.expand(list(RolesManager.get_roles_names()))
    def test_form_valid_match_role(self, role):
        data = {
            'first_name': 'test',
            'email': 'test@email.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'role': RolesManager.retrieve_role(role).get_name(),
        }
        form = self.view.form_class(data)
        form.full_clean()
        resp = self.view().form_valid(form)

        self.assertEqual(302, resp.status_code)

    def test_form_invalid_role(self):
        data = {
            'first_name': 'test',
            'email': 'test@email.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'role': list(RolesManager.get_roles())[0].get_name(),
        }
        form = self.view.form_class(data)
        form.full_clean()
        form.cleaned_data['role'] = 'invalid'
        resp = self.view().form_valid(form)

        self.assertEqual(400, resp.status_code)
