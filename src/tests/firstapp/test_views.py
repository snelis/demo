from django.test import TestCase


class TestViews(TestCase):

    def test_calc(self):
        self.assertEqual(4, 2*2)