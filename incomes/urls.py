from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeListViewSet, IncomeView, IncomeCreateView, IncomeUpdateView, IncomeDeleteView


router = DefaultRouter()

router.register('list', IncomeListViewSet, basename='incomes')

urlpatterns = [
    path('', include(router.urls)),
    path('view/<int:pk>/', IncomeView.as_view(), name='view-income'),
    path('create/', IncomeCreateView.as_view(), name='create-income'),
    path('update/<int:pk>/', IncomeUpdateView.as_view(), name='update-income'),
    path('delete/<int:pk>/', IncomeDeleteView.as_view(), name='delete-income'),
]
