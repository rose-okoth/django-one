from django.test import TestCase
from .models import Editor,Post,tags

# Create your tests here.
class EditorTestClass(TestCase):

# Set up method
    def setUp(self):
        self.rose= Editor(first_name = 'Rose', last_name ='Okoth', email ='okoth.rose@gmail.com')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rose,Editor))

# Testing Save Method
    def test_save_method(self):
        self.rose.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)