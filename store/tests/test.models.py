 
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Animal, Category


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='Konji', slug='konji')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'Konji')


class TestAnimalModel(TestCase):
    def setUp(self):
        Category.objects.create(name='Konji', slug='konji')
        User.objects.create(username='milan')
        self.data1 = Animal.objects.create(category_id=1, title='Toplokrvni konji', created_by_id=1,
                                            slug='toplokrvni-konji', price='20.00', image='konji')

    
    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Animal))
        self.assertEqual(str(data), 'Toplokrvni konji')