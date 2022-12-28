from django import forms
from .models import Post, Comment

"""
A class for posting a post with an image and caption
""" 
class PostImageForm(forms.ModelForm):
    class Meta:
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
        fields = ['caption',]

# """
# A class for updating user post
# """ 
# class EditComment(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['caption']