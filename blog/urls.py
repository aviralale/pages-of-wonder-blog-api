from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet, BlogViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('posts', BlogViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]