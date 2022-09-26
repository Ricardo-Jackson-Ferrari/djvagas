from django.test import TestCase
from project.job.facade import job_list
from project.job.models import Job


class JobListUnittest(TestCase):
    def test_job_list_return(self):
        self.assertQuerysetEqual(
            Job.objects.filter(status=True),
            job_list()
        )