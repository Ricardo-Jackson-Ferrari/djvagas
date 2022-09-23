from django.test import TestCase
from model_bakery import baker


class SchoolingUnittest(TestCase):
    def test_return_str(self):
        schooling = baker.make('Schooling')
        self.assertEqual(schooling.schooling, str(schooling))
