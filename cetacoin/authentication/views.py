from . import params
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
#Account creation for algorant network
from algosdk import account, encoding, mnemonic, algod
#from bitcoinlib import wallets
# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        with transaction.atomic():
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                new_user = serializer.save()
                if new_user:
                    # Creating Wallet from bitcoinlib wallet
                    #w = wallets.Wallet.create("Wallet" + str(new_user.id)+"BTC")
                    # create a algod client
                    acl = algod.AlgodClient(params.algod_token, params.algod_address)
                    # generate an account
                    private_key, address = account.generate_account()
                    # extract the mnemonic phrase from the private key
                    mn = mnemonic.from_private_key(private_key)
                    wallet_dict = {
                        #"idWallet": "Wallet" + str(new_user.id)+"BTC",
                        "idWallet": mn,
                        "amount": 0,
                        "currency": "algos",
                        "alias": "alias",
                        "user": new_user.id,
                    }
                    wallet_serializer = WalletSerializer(data=wallet_dict)
                    #print(wallet_serializer)
                    if wallet_serializer.is_valid():
                        # Saving wallet object associated for the user
                        wallet_serializer.save()
                        data = {
                            "user_data": serializer.data,
                            "wallet_data": wallet_serializer.data,
                            #"wallet_bitcoinb": w.as_json(),
                            "wallet_bitcoinb":acl.account_info(address),
                        }
                        return Response(data, status=status.HTTP_201_CREATED)
                    # deleting new user if the default wallet could not be createad
                    #wallets.wallet_delete_if_exists("Wallet" + str(new_user.id)+"BTC")
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
