from django.test import TestCase

# Create your tests here.

class SampleTestCase(TestCase):
    def test_sum(self):
        x = 1
        y = 2
        self.assertEqual(x+y, 3)