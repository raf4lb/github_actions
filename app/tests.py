from django.test import TestCase

from app.models import SimpleModel


class SampleTestCase(TestCase):
    def test_sum(self):
        x = 1
        y = 2
        self.assertEqual(x+y, 3)


class SimpleModelTestCase(TestCase):
    def test_model_creation(self):
        SimpleModel.objects.create(name='test')
        self.assertEqual(SimpleModel.objects.count(), 1)
        simple_model = SimpleModel.objects.first()
        self.assertEqual(simple_model.name, 'test')
