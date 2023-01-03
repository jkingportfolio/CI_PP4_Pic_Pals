"""
A module for models in the post app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
import uuid
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Post(models.Model):
    """
    A class for creating a post object
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='user_post',
                             on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=False)
    caption = models.TextField(default='Please enter caption.')
    caption_edited = models.BooleanField(default=False)
    caption_edited_time = models.DateTimeField(blank=True, null=True)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_date']

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[str(self.id)])


class Like(models.Model):
    """
    A class for creating a like object
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_likes")

    def __str__(self):
        return f'{self.user} liked {self.post}'


class Comment(models.Model):
    """
    A class for creating a comment object
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comment")
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'{self.user} commented on post {self.post}'
