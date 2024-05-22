from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import SavingsGoal
from users.models import UserProfile
from .serializers import SavingsGoalSerializer, SavingsGoalCreateSerializer


class SavingsGoalListViewSet(ModelViewSet):
    serializer_class = SavingsGoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SavingsGoal.objects.filter(user=self.request.user.profile)


class SavingsGoalView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        user = UserProfile.objects.get(user=request.user)
        savings_goal = SavingsGoal.objects.get(pk=pk)

        if savings_goal.user != user:
            return Response({'message': 'You are not authorized to view this savings goal!'}, status=status.HTTP_403_FORBIDDEN)

        serializer = SavingsGoalSerializer(savings_goal)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SavingsGoalCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = UserProfile.objects.get(user=request.user)
        serializer = SavingsGoalCreateSerializer(data=request.data)
        available_balance = request.user.profile.available_balance
        if serializer.is_valid():
            serializer.validated_data['user'] = user
            serializer.validated_data['current_amount'] = available_balance
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SavingsGoalUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        user = UserProfile.objects.get(user=request.user)
        savings_goal = SavingsGoal.objects.get(pk=pk)

        if savings_goal.user != user:
            return Response({'message': 'You are not authorized to update this savings goal!'}, status=status.HTTP_403_FORBIDDEN)

        serializer = SavingsGoalCreateSerializer(
            savings_goal, data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SavingsGoalDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        user = UserProfile.objects.get(user=request.user)
        savings_goal = SavingsGoal.objects.get(pk=pk)

        if savings_goal.user != user:
            return Response({'message': 'You are not authorized to delete this savings goal!'}, status=status.HTTP_403_FORBIDDEN)

        savings_goal.delete()
        return Response({'message': 'Savings goal deleted!'}, status=status.HTTP_200_OK)
