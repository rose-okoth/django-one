from django.contrib import admin
from .models import Editor,Post,tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags')

# Register your models here.
admin.site.register(Editor)
admin.site.register(Post)
admin.site.register(tags)

