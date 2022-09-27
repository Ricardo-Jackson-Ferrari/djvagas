from django.test import TestCase
from django.utils.translation import gettext_lazy as _
from parameterized import parameterized
from pytest import mark

from project.job.forms import JobCreateForm


@mark.unit
class JobCreateFormUnitTest(TestCase):
    @parameterized.expand(
        [
            ('title', _('job title')),
        ]
    )
    def test_field_placeholder(self, field, placeholder_test):
        form = JobCreateForm()
        placeholder_field = form[field].field.widget.attrs['placeholder']
        self.assertEqual(placeholder_test, placeholder_field)
