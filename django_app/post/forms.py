from django import forms

from post.models import Post


class PostForm(forms.ModelForm):
    comment = forms.CharField(max_length=100)
    photo = forms.ImageField()
