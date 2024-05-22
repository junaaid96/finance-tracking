from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Expense
from users.models import UserProfile
from transactions.models import Transaction
from .serializers import ExpenseSerializer, ExpenseCreateSerializer


class ExpenseListViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user.profile)


class ExpenseView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        user = UserProfile.objects.get(user=request.user)
        expense = Expense.objects.get(pk=pk)

        if expense.user != user:
            return Response({'message': 'You are not authorized to view this expense!'}, status=status.HTTP_403_FORBIDDEN)

        serializer = ExpenseSerializer(expense)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
                user=user, type='Expense', description=f"Your account debited by ${amount}.")

            user.save()

            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        user = UserProfile.objects.get(user=request.user)
        expense = Expense.objects.get(pk=pk)

        if expense.user != user:
            return Response({'message': 'You are not authorized to update this expense!'}, status=status.HTTP_403_FORBIDDEN)

        serializer = ExpenseCreateSerializer(expense, data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']

            if user.available_balance + expense.amount < amount:
                return Response({'message': 'Insufficient balance!'}, status=status.HTTP_400_BAD_REQUEST)

            user.available_balance += expense.amount - amount

            Transaction.objects.create(
                user=user, type='Expense Updated', description=f"Expense Id: {expense.id} updated with ${amount}.")

            user.save()

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        user = UserProfile.objects.get(user=request.user)
        expense = Expense.objects.get(pk=pk)

        if expense.user != user:
            return Response({'message': 'You are not authorized to delete this expense!'}, status=status.HTTP_403_FORBIDDEN)

        user.available_balance += expense.amount
        user.save()
        expense.delete()

        Transaction.objects.create(
            user=user, type='Expense Deleted', description=f"Expense Id: {expense.id} with ${expense.amount} deleted and returned back to your account.")

        return Response({'message': 'Expense deleted successfully!'}, status=status.HTTP_200_OK)
