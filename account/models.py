from django.db import models
from django import settings
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    profile_pic = CloudinaryField(blank=True, default='default_profile_pic.jpeg')

    def __str__(self):
        return f'Profile of {self.user.username}'