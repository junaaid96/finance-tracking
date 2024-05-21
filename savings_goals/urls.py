from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SavingsGoalViewSet, SavingsGoalCreateView

router = DefaultRouter()

router.register('list', SavingsGoalViewSet, basename='savings-goals')

urlpatterns = [
    path('', include(router.urls)),
    path('create/', SavingsGoalCreateView.as_view(), name='create'),
]
