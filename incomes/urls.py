from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, IncomeCreateView


router = DefaultRouter()

router.register('list', IncomeViewSet, basename='incomes')

urlpatterns = [
    path('', include(router.urls)),
    path('create/', IncomeCreateView.as_view(), name='create-income'),
]
