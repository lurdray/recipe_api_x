
from rest_framework import serializers 
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()
  
class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=300)
    account_type = serializers.CharField(max_length=100)


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User 
        fields = "__all__"

