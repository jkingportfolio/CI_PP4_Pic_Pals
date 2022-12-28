from django.contrib import admin
from .models import Profile, Follow

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'dob', 'profile_pic', 'bio']
    raw_id_fields = ['user']

@admin.register(Follow)
class PostAdmin(admin.ModelAdmin):
    list_display = ['created', 'user', 'followed_account']
