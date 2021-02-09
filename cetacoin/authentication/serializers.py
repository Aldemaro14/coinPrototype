from rest_framework import serializers
from authentication.models import UserCrypto
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        # print(user)
        # print(user.email)
        # print(user.username)
        token['email'] = str(user.email)
        token['first_name'] = str(user.first_name)
        token['last_name'] = str(user.last_name)
        # print(token['email'])
        # print(type(token))
        return token
    # def get_tokens_for_user(user):
    #     refresh = RefreshToken.for_user(user)
    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token),
    #         'email': "hola"
    #     }


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
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
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=2)

    class Meta:
        model = UserCrypto
        fields = ['email', 'password']
