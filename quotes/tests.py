from django.test import TestCase
from .models import Editor,Post,tags

# Create your tests here.
class EditorTestClass(TestCase):

# Set up method
    def setUp(self):
        self.james= Editor(first_name = 'Rose', last_name ='Okoth', email ='okoth.rose@gmail.com')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))