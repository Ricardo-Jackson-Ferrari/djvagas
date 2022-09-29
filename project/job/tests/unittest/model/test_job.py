from django.test import TestCase
from model_bakery import baker
from pytest import mark


@mark.unit
class SchoolingUnittest(TestCase):
    def test_return_str(self):
        job = baker.make('Job')
        self.assertEqual(job.title, str(job))
