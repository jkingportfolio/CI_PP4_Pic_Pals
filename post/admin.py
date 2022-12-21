from django.contrib import admin
from .models import Post, Follow, Feed, Like, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['image', 'created_date']
    list_filter = ['created_date']

@admin.register(Follow)
class PostAdmin(admin.ModelAdmin):
    list_display = ['created', 'follower', 'following']

admin.site.register(Feed)
admin.site.register(Like)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['created_on', 'user', 'post', 'comment_body']