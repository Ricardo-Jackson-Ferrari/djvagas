from django.contrib.auth import get_user_model
from django.test import TestCase
from faker import Faker
from parameterized import parameterized
from pytest import mark

from project.account.managers import UserManager


@mark.unit
class UserManagerUnittest(TestCase):
    def setUp(self) -> None:
        self.usermanager = UserManager()
        self.usermanager.model = get_user_model()
        self.email = f'{Faker().first_name()}@email.com'
        self.password = self.usermanager.make_random_password()

    def test_create_user_success(self):
        user = self.usermanager.create_user(
            email=self.email, password=self.password
        )

        self.assertIsNotNone(user)

    def test_create_user_raise_value_error(self):
        kwargs = {'email': '', 'password': self.password}
        self.assertRaises(ValueError, self.usermanager.create_user, **kwargs)

    def test_create_super_user_success(self):
        user = self.usermanager.create_superuser(
            email=self.email, password=self.password
        )

        self.assertIsNotNone(user)

    @parameterized.expand(
        [
            ({'is_staff': False},),
            ({'is_superuser': False},),
        ]
    )
    def test_create_super_user_raise_value_error(self, extra_field):
        kwargs = {
            'email': self.email,
            'password': self.password,
            **extra_field,
        }
        self.assertRaises(
            ValueError, self.usermanager.create_superuser, **kwargs
        )
