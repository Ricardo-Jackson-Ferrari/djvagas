from django.test import TestCase
from model_bakery import baker


class SchoolingUnittest(TestCase):
    def test_return_str(self):
        application = baker.make('Application')
        self.assertEqual(application.job.title, str(application))
