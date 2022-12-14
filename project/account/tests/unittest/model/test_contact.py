from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils.translation import gettext_lazy as _
from model_bakery import baker
from pytest import mark

from project.account.models import Contact


@mark.unit
class ContactUnittest(TestCase):
    def test_return_str(self):
        contact = baker.prepare(Contact)
        self.assertEqual(contact.phone, str(contact))

    def test_def_clean_ok(self):
        user = baker.make(get_user_model(), id=1)
        data = {
            'user': user,
            'phone': '21999999999',
        }

        contact = Contact(**data)

        self.assertIsNone(contact.clean())

    def test_def_clean_error(self):
        user = baker.make(get_user_model())

        for x in range(2):
            baker.make(Contact, user=user, phone=f'{x}')

        contact = baker.prepare(Contact, user=user)

        self.assertRaises(ValidationError, contact.clean)

    def test_unique_error_message(self):
        unique_check = ('user', 'phone')
        msg = _('%(phone)s already registered for this user.')
        contact = baker.prepare(Contact)
        error = contact.unique_error_message(
            model_class=Contact, unique_check=unique_check
        )
        self.assertEqual(msg, error.message)
