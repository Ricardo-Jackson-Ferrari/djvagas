from django.test import TestCase
from django.utils.translation import gettext_lazy as _
from model_bakery import baker
from parameterized import parameterized
from pytest import mark

from project.job.models import Application


@mark.unit
class SchoolingUnittest(TestCase):
    def test_return_str(self):
        application = baker.make(Application)
        self.assertEqual(application.job.title, str(application))

    @parameterized.expand(
        [
            (
                _('%(model_name)s with this %(field_labels)s already exists.'),
                ('schooling', 'job'),
            ),
            (
                _('%(candidate)s already registered for job.'),
                ('candidate', 'job'),
            ),
        ]
    )
    def test_unique_error_message(self, msg, unique_check):
        application = baker.make(Application)
        error = application.unique_error_message(
            model_class=Application, unique_check=unique_check
        )
        self.assertEqual(msg, error.message)
