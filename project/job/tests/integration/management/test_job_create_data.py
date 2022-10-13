from django.core.management import call_command
from django.test import TestCase

from project.job.models import Job


class JobCreateDataTest(TestCase):
    def test_database_persistence(self):
        call_command('job_create_data')
        self.assertEqual(10, Job.objects.all().count())
