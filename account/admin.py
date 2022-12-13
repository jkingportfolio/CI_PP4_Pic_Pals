from django.contrib import admin
from .models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['user','dob','profile_pic']
    raw_id_fields = ['user']
