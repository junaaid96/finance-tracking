from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, UserRegistrationViewSet, UserLoginViewSet, UserLogoutViewSet

router = DefaultRouter()

router.register('list', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationViewSet.as_view(), name='register'),
    path('login/', UserLoginViewSet.as_view(), name='login'),
    path('logout/', UserLogoutViewSet.as_view(), name='logout'),
]
