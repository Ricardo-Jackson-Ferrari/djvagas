from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker
from pytest import mark


@mark.unit
class UserModelUnittest(TestCase):
    def setUp(self) -> None:
        self.user = baker.make(get_user_model())

    def test_user_model_def_get_short_name(self):
        self.assertEqual(self.user.first_name, self.user.get_short_name())

    def test_user_model_def_get_full_name(self):
        self.assertEqual(self.user.first_name, self.user.get_full_name())

    def test_user_model_def_clean(self):
        self.user = baker.make(get_user_model(), email='EXAMPLE@EXAMPLE.COM')
        email_clean = (
            self.user.email.split('@')[0]
            + '@'
            + self.user.email.split('@')[1].lower()
        )
        self.user.clean()
        self.assertEqual(email_clean, self.user.email)

    def test_user_model_def_email_user(self):
        self.assertEqual(1, self.user.email_user('teste', 'teste'))
