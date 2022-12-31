from django import forms
from .models import Post, Comment
from crispy_forms.helper import FormHelper

"""
A class for posting a post with an image and caption
"""


class PostImageForm(forms.ModelForm):
    class Meta:

        def __init__(self, *args, **kwargs):
            super(PostImageForm, self).__init__(*args, **kwargs)
            self.helper.form_show_labels = False

        model = Post
        fields = ['image', 'caption']


"""
A class for posting a comment to a post
"""


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body']


"""
A class for updating user post
"""


class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption']

# """
# A class for updating user post
# """
# class EditComment(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['caption']
