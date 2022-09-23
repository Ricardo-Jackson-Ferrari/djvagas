from django.test import TestCase
from model_bakery import baker


class SchoolingUnittest(TestCase):
    def test_return_str(self):
        job = baker.make('Job')
        self.assertEqual(job.title, str(job))
