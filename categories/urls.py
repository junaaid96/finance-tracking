from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryListViewSet

router = DefaultRouter()

router.register('list', CategoryListViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]
