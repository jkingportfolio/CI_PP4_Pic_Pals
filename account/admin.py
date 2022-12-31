# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal
from .models import Profile, Follow
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin class for a users profile object
    """
    list_display = (
        'user',
        'date_of_birth',
        'profile_pic',
        'bio'
        )
    search_fields = [
        'user',
        'date_of_birth',
        'profile_pic',
        'bio'
        ]           
    raw_id_fields = [
        'user'
        ]


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """
    Admin class for a post object
    """
    list_display = (
        'created',
        'user',
        'followed_account'
        )
