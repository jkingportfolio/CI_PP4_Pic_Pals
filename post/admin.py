from django.contrib import admin
from .models import Post, Follow, Feed

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['image', 'created_date']
    list_filter = ['created_date']

admin.site.register(Follow)
admin.site.register(Feed)