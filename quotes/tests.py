from django.test import TestCase
from .models import Editor,Post,tags
import datetime as dt

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

        self.new_post= Post(title = 'Test Post',quote = 'This is a random test Post',editor = self.rose)
        self.new_post.save()

        self.new_post.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Post.objects.all().delete()

    def test_get_quotes_today(self):
        today_quotes = Post.todays_quotes()
        self.assertTrue(len(today_quotes)>0)

    def test_get_quotes_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        quotes_by_date = Post.days_quotes(date)
        self.assertTrue(len(quotes_by_date) == 0)