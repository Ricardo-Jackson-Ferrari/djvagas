from django.test import TestCase

from project.job.facade import get_job_list
from project.job.views import JobList


class JobListUnittest(TestCase):
    def test_job_list_get_queryset(self):
        self.assertQuerysetEqual(get_job_list(), JobList().get_queryset())
