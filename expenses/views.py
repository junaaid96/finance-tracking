from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Expense
from users.models import UserProfile
from transactions.models import Transaction
from .serializers import ExpenseSerializer, ExpenseCreateSerializer


class ExpenseViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user.profile)


class ExpenseCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = UserProfile.objects.get(user=request.user)
        return Response({'user': user.user.first_name + " "+user.user.last_name, 'available_balance': user.available_balance}, status=status.HTTP_200_OK)

    def post(self, request):
        user = UserProfile.objects.get(user=request.user)
        serializer = ExpenseCreateSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            
            if user.available_balance < amount:
                return Response({'message': 'Insufficient balance!'}, status=status.HTTP_400_BAD_REQUEST)

            user.available_balance -= amount

            Transaction.objects.create(
                user=user, amount=amount, type='Expense')
            
            user.save()

            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
