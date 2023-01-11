from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, ImageSerializer, PostSerializer, TagSerializer
from .models import Category, Post


# ______________________________USER_______________________________________
class PostsViewSet(ModelViewSet):
    authentication_classes = []
    serializer_class = PostSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Post.objects.filter(category=category)

    def get_serializer_context(self):
        return {'request': self.request}


class CategoriesViewSet(ModelViewSet):
    authentication_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_context(self):
        return {'request':self.request}
