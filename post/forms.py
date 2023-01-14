"""
A module for forms in the post app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django import forms
# Internal
from .models import Post, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PostImageForm(forms.ModelForm):
    """
    A class for posting a post with an image and caption
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['caption'].widget = forms.Textarea(
            attrs={'placeholder': 'Write a little about this image.'})

    class Meta:
        model = Post
        fields = ['image', 'caption']


class PostCommentForm(forms.ModelForm):
    """
    A class for posting a comment to a post
    """
    class Meta:
        model = Comment
        fields = ['comment_body']


class EditPost(forms.ModelForm):
    """
    A class for updating user post
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['caption'].widget = forms.Textarea(
            attrs={'placeholder': 'Write a little about this image.'})

    class Meta:
        model = Post
        fields = ['caption']
