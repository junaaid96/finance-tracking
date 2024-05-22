from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseListViewSet, ExpenseView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView


router = DefaultRouter()

router.register('list', ExpenseListViewSet, basename='expenses')

urlpatterns = [
    path('', include(router.urls)),
    path('view/<int:pk>/', ExpenseView.as_view(), name='view-expense'),
    path('create/', ExpenseCreateView.as_view(), name='create-expense'),
    path('update/<int:pk>/', ExpenseUpdateView.as_view(), name='update-expense'),
    path('delete/<int:pk>/', ExpenseDeleteView.as_view(), name='delete-expense'),
]
