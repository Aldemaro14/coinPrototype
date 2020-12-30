from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    firstName = serializers.CharField(max_length=255, min_length=2)
    lastName = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = UserCrypto
        fields = ['firstName', 'lastName', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if UserCrypto.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    #username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = UserCrypto
        fields = ['email', 'password']

        def validate(self, attrs):
            email = attrs.get('email', '')
            try:
                UserCrypto.objects.filter(email=email).exist()
            except UserCrypto.DoesNotExist:
                raise serializers.ValidationError(
            {'email' : ('Email does not exist')})
            return super().validate(attrs)