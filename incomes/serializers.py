from rest_framework import serializers
from .models import Income


class IncomeSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Income
        fields = '__all__'


class IncomeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['amount', 'category', 'description']
