from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from post.models import Post


"""
Class for creating a users profile
""" 
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_pic = CloudinaryField(blank=True)
    bio = models.CharField(max_length=5000, blank=True)
    # location with google maps api to potentially be future implemented

    def __str__(self):
        return f'Profile of {self.user.username}'

"""
Class for creating follow objects
""" 
class Follow(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user')
    followed_account = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='follow_account')
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user} followed {self.followed_account}'

# Dynamically add following field to User
# Credits to Django 4 by Example by Antonio Mele
user_model = get_user_model()
user_model.add_to_class('following',
                        models.ManyToManyField('self',
                            through=Follow,
                            related_name='followers',
                            symmetrical=False))
