from django.urls import path, include
from rest_framework_nested import routers

from .views import PostsViewSet, CategoriesViewSet

router = routers.DefaultRouter()
router.register('categories', CategoriesViewSet, basename='categroies')
article_router = routers.NestedDefaultRouter(router, 'categories', lookup='category')
article_router.register('posts', PostsViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(article_router.urls)),
]
