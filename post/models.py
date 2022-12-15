from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_post', on_delete=models.CASCADE)
    description = models.CharField(max_length=10000, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    post_image = CloudinaryField('image', default='placeholder')
    created_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_like', blank=True)
    # location = to be implemented in the future

    class Meta:
        ordering = ['-created_date'],
        indexes = [models.Index(fields=['-created_date'])]

