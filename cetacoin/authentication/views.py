from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer, MyTokenObtainPairSerializer, WalletSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from rest_framework.permissions import AllowAny
import jwt
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db import transaction
# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        with transaction.atomic():
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                new_user = serializer.save()
                if new_user:
                    print(serializer)
                    wallet_dict = {
                        "idWallet": 2,
                        "amount": 0,
                        "currency": "bitcoin",
                        "test": "test",
                        "user": new_user.id,
                    }
                    wallet_serializer = WalletSerializer(data=wallet_dict)
                    print(wallet_serializer)
                    if wallet_serializer.is_valid():
                        wallet_serializer.save()
                        data = {
                            "user_data": serializer.data,
                            "wallet_data": wallet_serializer.data,
                        }
                        return Response(data, status=status.HTTP_201_CREATED)
                    # deleting new user if the default wallet could not be createad
                    new_user.delete()
                    return Response(wallet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if user:
            auth_token = jwt.encode(
                {'email': user.email}, settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
