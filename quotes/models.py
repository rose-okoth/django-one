from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class tags(models.Model):
    '''
    Class for the tags of the quotes.
    '''
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Post(models.Model):
    '''
    Class for the quote posts.
    '''
    title = models.CharField(max_length =60)
    quote = HTMLField()
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'posts/', default='default.jpg')

    @classmethod
    def todays_quotes(cls):
        today = dt.date.today()
        quotes = cls.objects.filter(pub_date__date = today)
        return quotes

    @classmethod
    def days_quotes(cls,date):
        quotes = cls.objects.filter(pub_date__date = date)
        return quotes

    @classmethod
    def search_by_title(cls,search_term):
        quotes = cls.objects.filter(title__icontains=search_term)
        return quotes