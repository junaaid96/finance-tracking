from rest_framework import serializers
from .models import SavingsGoal


class SavingsGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsGoal
        fields = '__all__'


class SavingsGoalCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavingsGoal
        fields = ['name', 'amount', 'deadline']
