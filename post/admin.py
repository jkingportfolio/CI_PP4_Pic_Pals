from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['created_date', 'post_image', 'caption']
    list_filter = ['created_date']
