from rest_framework import serializers
from django.contrib.auth.models import User
from authentication.models import UserCrypto
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, UserCrypto):
        token = super(MyTokenObtainPairSerializer, cls).get_token(UserCrypto)

        # Add custom claims
        token['email'] = UserCrypto.email
        return token

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = UserCrypto
        fields = ['first_name', 'last_name', 'email', 'password']


    def validate(self, attrs):
        email = attrs.get('email', '')
        if UserCrypto.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)



    def create(self, validated_data):
        return UserCrypto.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=2)

    class Meta:
        model = UserCrypto
        fields = ['email', 'password']


