from django.contrib import admin
from .models import Post, Like, Comment


"""
Admin class for a post
""" 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['image', 'created_date']
    list_filter = ['created_date']


"""
Admin class for a like object
""" 
admin.site.register(Like)


"""
Admin class for a comment object
""" 
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['created_on', 'user', 'post', 'comment_body']