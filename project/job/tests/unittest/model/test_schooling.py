from django.test import SimpleTestCase
from model_bakery import baker
from pytest import mark


@mark.unit
class SchoolingUnittest(SimpleTestCase):
    def test_return_str(self):
        schooling = baker.prepare('Schooling')

        self.assertEqual(schooling.schooling, str(schooling))

    def test_operator_gt(self):
        schooling_low_level = baker.prepare('Schooling', level=0)
        schooling_high_level = baker.prepare('Schooling', level=1)

        self.assertTrue(schooling_high_level > schooling_low_level)
        self.assertFalse(schooling_high_level < schooling_low_level)

    def test_operator_ge(self):
        schooling_low_level_one = baker.prepare('Schooling', level=0)
        schooling_low_level_second = baker.prepare('Schooling', level=0)
        schooling_high_level = baker.prepare('Schooling', level=1)

        self.assertTrue(schooling_low_level_one >= schooling_low_level_second)
        self.assertFalse(schooling_high_level <= schooling_low_level_one)

    def test_operator_eq(self):
        schooling_low_level_one = baker.prepare('Schooling', level=0)
        schooling_low_level_second = baker.prepare('Schooling', level=0)
        schooling_high_level = baker.prepare('Schooling', level=1)

        self.assertTrue(schooling_low_level_one == schooling_low_level_second)
        self.assertFalse(schooling_low_level_one == schooling_high_level)
