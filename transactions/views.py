from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user.profile)
    
