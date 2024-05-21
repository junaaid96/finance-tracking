from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllUserProfileViewSet, UserProfileViewSet, UserRegistrationViewSet, UserLoginViewSet, UserLogoutViewSet

router = DefaultRouter()

router.register('list', AllUserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profile/<int:user_id>/', UserProfileViewSet.as_view(), name='user-profile'),
    path('register/', UserRegistrationViewSet.as_view(), name='register'),
    path('login/', UserLoginViewSet.as_view(), name='login'),
    path('logout/', UserLogoutViewSet.as_view(), name='logout'),
]
