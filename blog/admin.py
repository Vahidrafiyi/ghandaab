from django.contrib import admin
from django.contrib.admin import register

from .models import Category, Post, Image, Tag


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
