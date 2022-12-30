from django.contrib import admin
from .models import Profile, Follow

# Register your models here.

"""
Admin class for a users profile object
""" 
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'date_of_birth', 'profile_pic', 'bio']
    raw_id_fields = ['user']

"""
Admin class for a post object
""" 
@admin.register(Follow)
class PostAdmin(admin.ModelAdmin):
    list_display = ['created', 'user', 'followed_account']
