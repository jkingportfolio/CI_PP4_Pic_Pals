"""
A module for forms
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
    class Meta:
        model = Post
        fields = ['caption']
