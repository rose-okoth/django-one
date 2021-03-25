from .models import Post
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }