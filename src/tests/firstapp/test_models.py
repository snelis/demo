from django.test import TestCase
from firstapp.models import Shoe, Color


class ShoeTestCase(TestCase):

    def setUp(self):

        black = Color()
        black.color = 'black'
        black.save()

        for i in range(100):
            shoe = Shoe()
            shoe.size = i
            shoe.color = black
            shoe.save()

    def test_select(self):
        shoe = Shoe.objects.filter()

        self.assertIsInstance(shoe[0], Shoe)
        self.assertTrue(shoe)

    def test_model_query_set(self):

        blueish = Color()
        blueish.color = 'blueish'
        blueish.save()

        shoe = Shoe()
        shoe.size = 123
        shoe.color = blueish
        shoe.save()

        shoe = Shoe.objects.get_query_set().size(123).color('blueish')[0]
        self.assertTrue(shoe)

        self.assertEqual(shoe.size, 123)
        self.assertEqual(shoe.color.color, 'blueish')
