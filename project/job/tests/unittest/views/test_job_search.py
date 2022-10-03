from django.http import Http404, HttpRequest, QueryDict
from django.test import TestCase
from model_bakery import baker
from pytest import mark

from project.job.views import JobSearch


@mark.unit
class JobSearchUnittest(TestCase):
    def setUp(self) -> None:
        self.view = JobSearch()
        self.view.request = HttpRequest()

    def test_job_search_get_queryset(self):
        baker.make(
            'Job', checked=True, status=True, title='test', description='test'
        )
        baker.make(
            'Job',
            checked=True,
            status=True,
            title='another',
            description='another',
        )

        self.view.request.GET = QueryDict('q=test')

        self.assertEqual(1, self.view.get_queryset().count())

    def test_job_search_get_queryset_not_search_term(self):
        self.assertRaises(Http404, self.view.get_queryset)
