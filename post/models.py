from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_post', on_delete=models.CASCADE)
    caption = models.CharField(max_length=10000, blank=True)
    post_image = CloudinaryField('image', default='placeholder')
    created_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_like', blank=True)
    # location = to be implemented in the future

    class Meta:        
        # indexes = [models.Index(fields=['-created_date'])]
        ordering = ['-created_date']

    def __str__(self):
        return self.caption
