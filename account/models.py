from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from post.models import Post, Follow

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    profile_pic = CloudinaryField(blank=True)
    # bio = models.CharField(max_length=5000, blank=True)
    # location with google maps api to potentially be future implemented

    def __str__(self):
        return f'Profile of {self.user.username}'

# Dynamic user following field

user_model = get_user_model()
user_model.add_to_class(
    'accounts_following', models.ManyToManyField('self', through=Follow, related_name='followers', symmetrical=False))
