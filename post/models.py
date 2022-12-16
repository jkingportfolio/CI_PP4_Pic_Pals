from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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
        # indexes = [models.Index(fields=['-created_date'])]
        ordering = ['-created_date']

    # Automatically generate slug based on title field
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


