from rest_framework.serializers import ModelSerializer
from .models import Category, Image, Post, Tag


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']

class CategorySerializer(ModelSerializer):
    image = ImageSerializer()
    class Meta:
        model = Category
        fields = ['id', 'title', 'image']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

class RelatedPostsSerializer(ModelSerializer):
    main_image = ImageSerializer()
    class Meta:
        model = Post
        fields = ['id', 'title', 'subtitle', 'main_image']


class PostSerializer(ModelSerializer):
    main_image = ImageSerializer()
    body_images = ImageSerializer(many=True)
    category = CategorySerializer()
    related_posts = RelatedPostsSerializer(many=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'subtitle', 'body',
         'main_image', 'body_images', 'author', 'category',
          'tags', 'related_posts', 'status', 'created_at', 'updated_at']