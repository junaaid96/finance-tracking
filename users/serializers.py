from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    first_name = serializers.CharField(
        source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'confirm_password', 'phone_number', 'address']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError(
                {'password': 'Passwords must match!'})

        if User.objects.filter(username=user.username).exists():
            raise serializers.ValidationError(
                {'username': 'Username already exists!'})

        if User.objects.filter(email=user.email).exists():
            raise serializers.ValidationError(
                {'email': 'Email already exists!'})

        user.set_password(password)
        user.save()

        UserProfile.objects.create(
            user=user,
            phone_number=self.validated_data['phone_number'],
            address=self.validated_data['address']
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
