from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SavingsGoalListViewSet, SavingsGoalView, SavingsGoalCreateView, SavingsGoalUpdateView, SavingsGoalDeleteView

router = DefaultRouter()

router.register('list', SavingsGoalListViewSet, basename='savings-goals')

urlpatterns = [
    path('', include(router.urls)),
    path('view/<int:pk>/', SavingsGoalView.as_view(), name='view'),
    path('create/', SavingsGoalCreateView.as_view(), name='create'),
    path('update/<int:pk>/', SavingsGoalUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', SavingsGoalDeleteView.as_view(), name='delete'),
]
