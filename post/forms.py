from django import forms
from .models import Post, Comment


class PostImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body']