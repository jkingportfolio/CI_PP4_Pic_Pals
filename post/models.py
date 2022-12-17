from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid

# Create your models here.



class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_post', on_delete=models.CASCADE)
    post_image = CloudinaryField('image', default='placeholder')
    caption = models.TextField(default='Please enter caption.')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user
