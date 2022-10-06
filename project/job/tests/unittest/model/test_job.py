from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from model_bakery import baker
from pytest import mark

from project.job.models import Job


@mark.unit
class JobUnittest(TestCase):
    def test_return_str(self):
        job = baker.make('Job')
        self.assertEqual(job.title, str(job))

    def test_def_clean_error(self):
        data = {
            'title': 'test',
            'status': True,
            'checked': True,
            'slug': 'test',
            'schooling': baker.make('Schooling'),
            'salary_from': 1.0,
            'salary_to': 0.0,
            'company': baker.make(get_user_model()),
            'description': 'test',
        }

        job = Job(**data)

        self.assertRaises(ValidationError, job.clean)

    def test_def_clean_ok(self):
        data = {
            'title': 'test',
            'status': True,
            'checked': True,
            'slug': 'test',
            'schooling': baker.make('Schooling'),
            'salary_from': 0.0,
            'salary_to': 1.0,
            'company': baker.make(get_user_model()),
            'description': 'test',
        }

        job = Job(**data)

        self.assertIsNone(job.clean())
