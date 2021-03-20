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

class PostTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.rose= Editor(first_name = 'Rose', last_name ='Okoth', email ='okoth.rose@gmail.com')
        self.rose.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.rose)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Post.objects.all().delete()