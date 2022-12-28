from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.db.models.signals import post_save
import uuid


"""
Class for creating a post object
""" 
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_post', on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder')
    caption = models.TextField(default='Please enter caption.')
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_date']

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[str(self.id)])


"""
Class for creating a like object
""" 
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")

    def __str__(self):
        return f'{self.user} liked {self.post}'


"""
Class for creating a comment object
""" 
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'{self.user} commented on post {self.post}' 


