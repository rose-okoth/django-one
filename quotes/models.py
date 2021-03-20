from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length =60)
    quote = models.TextField()
    editor = models.ForeignKey('Editor', on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def todays_quotes(cls):
        today = dt.date.today()
        quotes = cls.objects.filter(pub_date__date = today)
        return quotes

    @classmethod
    def days_quotes(cls,date):
        quotes = cls.objects.filter(pub_date__date = date)
        return quotes