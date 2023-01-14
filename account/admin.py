"""
A module for admin i nthe account app
"""
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
        'date_of_birth'
        )
    search_fields = (
        'user',
        'date_of_birth'
        )
    list_filter = (
        'user',
        'date_of_birth'
        )
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
    list_filter = (
        'created',
        'user',
        'followed_account'
    )
