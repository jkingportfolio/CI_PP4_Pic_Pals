from django import forms
from .models import Post


class PostImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'post_image']