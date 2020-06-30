from django.test import TestCase
from . models import Products

class ProductTests(TestCase):
    def test_str(self):
        test_name = Products(name='A Product')
        self.assertEqal(str(test_name,'A Product'))

