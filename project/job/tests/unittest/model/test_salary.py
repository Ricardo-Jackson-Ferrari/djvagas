from django.test import TestCase
from model_bakery import baker
from pytest import mark


@mark.unit
class SchoolingUnittest(TestCase):
    def test_return_str(self):
        salary = baker.make('Salary')
        self.assertEqual(salary.salary_range, str(salary))
