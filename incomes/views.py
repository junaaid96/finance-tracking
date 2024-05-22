from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Income
from users.models import UserProfile
from transactions.models import Transaction
from .serializers import IncomeSerializer, IncomeCreateSerializer


class IncomeListViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IncomeSerializer

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user.profile)


class IncomeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        user = UserProfile.objects.get(user=request.user)
        income = Income.objects.get(pk=pk)

        if income.user != user:
            return Response({'message': 'You are not authorized to view this income!'}, status=status.HTTP_403_FORBIDDEN)

        serializer = IncomeSerializer(income)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IncomeCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = UserProfile.objects.get(user=request.user)
        return Response({'user': user.user.first_name + " "+user.user.last_name, 'available_balance': user.available_balance}, status=status.HTTP_200_OK)

    def post(self, request):
        user = UserProfile.objects.get(user=request.user)
        serializer = IncomeCreateSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']

            user.available_balance += amount

            Transaction.objects.create(
                user=user, type='Income', description=f"Your account credited by ${amount}.")

            user.save()
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomeUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        user = UserProfile.objects.get(user=request.user)
        income = Income.objects.get(pk=pk)

        if income.user != user:
            return Response({'message': 'You are not authorized to update this income!'}, status=status.HTTP_403_FORBIDDEN)

        serializer = IncomeCreateSerializer(income, data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']

            user.available_balance -= income.amount
            user.available_balance += amount

            Transaction.objects.create(
                user=user, type='Income Updated', description=f"Income Id: {pk} has been updated with ${amount}.")

            user.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomeDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        user = UserProfile.objects.get(user=request.user)
        income = Income.objects.get(pk=pk)

        if income.user != user:
            return Response({'message': 'You are not authorized to delete this income!'}, status=status.HTTP_403_FORBIDDEN)

        user.available_balance -= income.amount
        user.save()
        income.delete()

        Transaction.objects.create(
            user=user, type='Income Deleted', description=f"Income Id: {pk} with ${income.amount} has been deleted and deducted from your account balance.")

        return Response({'message': 'Income deleted successfully!'}, status=status.HTTP_200_OK)
