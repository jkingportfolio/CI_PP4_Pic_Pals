"""
A module for admin in the post app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal
from .models import Post, Like, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin class for a post
    """
    list_display = (
        'image',
        'created_date')
    list_filter = (
        'created_date',
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """
    Admin class for a like object
    """
    list_display = (
        'user',
        'post'
    )

    list_filter = (
        'user',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
        Admin class for a comment object
    """
    list_display = (
        'created_on',
        'user',
        'post',
        'comment_body'
    )
    list_filter = (
        'user',
    )
