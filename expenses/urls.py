from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, ExpenseCreateView


router = DefaultRouter()

router.register('list', ExpenseViewSet, basename='expenses')

urlpatterns = [
    path('', include(router.urls)),
    path('create/', ExpenseCreateView.as_view(), name='create-expense'),
]
