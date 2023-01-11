from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile

@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')

@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
