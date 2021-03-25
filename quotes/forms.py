from .models import Post
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [ 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }