from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.db.models.signals import post_save
import uuid

# Create your models here.



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


class Follow(models.Model):
    follower = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='following')
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.follower} follows {self.following}'

class Feed(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='feed_following')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()

    def add_post(sender, instance, *args, **kwargs):
        post = instance
        user = post.user
        followers = Follow.objects.all().filter(following=user)

        for follower in followers:
            feed = Feed(post=post, user=follower.follower, date=post.created_date, following=user)
            feed.save()


post_save.connect(Feed.add_post, sender=Post)
