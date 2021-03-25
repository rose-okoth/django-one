from django.test import TestCase
from .models import Post,tags
import datetime as dt
from django.contrib.auth.models import User

class UserTestClass(TestCase):

# Set up method
    def setUp(self):
        self.rose= User(first_name = 'Rose', last_name ='Okoth', email ='okoth.rose@gmail.com')

# Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rose,User))


class PostTestClass(TestCase):

    def setUp(self):
        # Creating a new user and saving it
        self.rose= User(first_name = 'Rose', last_name ='Okoth', email ='okoth.rose@gmail.com')

    def tearDown(self):
        User.objects.all().delete()
        tags.objects.all().delete()
        Post.objects.all().delete()

    def test_get_quotes_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        quotes_by_date = Post.days_quotes(date)
        self.assertTrue(len(quotes_by_date) == 0)