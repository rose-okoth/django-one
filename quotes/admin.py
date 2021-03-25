from django.contrib import admin
from .models import Post,tags

class PostAdmin(admin.ModelAdmin):
    filter_horizontal =('tags')

# Register your models here.
admin.site.register(Post)
admin.site.register(tags)

