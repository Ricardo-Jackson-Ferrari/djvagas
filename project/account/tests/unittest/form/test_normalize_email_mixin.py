from django.test import SimpleTestCase
from faker import Faker
from pytest import mark

from project.account.forms import NormalizeEmailMixin


@mark.unit
class NormalizeEmailMixinUnittest(SimpleTestCase):
    def test_normalize_email_set_email_string_to_lower(self):
        mixin = NormalizeEmailMixin()
        email = f'{Faker().first_name()}@email.com'.upper()
        mixin.data = {'email': email}
        mixin._normalize_email()

        self.assertEqual(email.lower(), mixin.data['email'])

    def test_normalize_email_when_email_is_none(self):
        mixin = NormalizeEmailMixin()
        mixin.data = {'email': None}
        mixin._normalize_email()

        self.assertEqual(None, mixin.data['email'])
