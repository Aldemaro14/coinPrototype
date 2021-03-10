from django.shortcuts import render
from authentication.models import UserCrypto, Wallet
from authentication import params
from authentication.serializers import WalletSerializer
#Rest-framework imports
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
#Account creation for algorant network
from algosdk import account, encoding, mnemonic, algod
#Transaction in views
from django.db import transaction
#Status in response
from rest_framework import status
from django.http import JsonResponse
# Create your views here.


class WalletCreationView(GenericAPIView):    
    serializer_class = WalletSerializer
    def post(self, request):
        with transaction.atomic():
            print(request.data)
            user=UserCrypto.objects.get(email= request.data['email'])
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
                "currency": request.data['currency'],
                "alias": "alias",
                "user": user.id,
            }
            wallet_serializer = WalletSerializer(data= wallet_dict)
            if wallet_serializer.is_valid():
                # Saving wallet object associated for the user
                wallet_serializer.save()
                data = {                    
                    "wallet_data": wallet_serializer.data,
                    #"wallet_bitcoinb": w.as_json(),
                    "wallet_crypto":acl.account_info(address),
                }
                return Response(data, status=status.HTTP_201_CREATED)           
            return Response(wallet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class WalletListView(GenericAPIView):    
    serializer_class = WalletSerializer
    def post(self, request):                            
            user=UserCrypto.objects.get(email= request.data['email'])
            wallets = Wallet.objects.filter(user=user.id)
            serializer = WalletSerializer(wallets, many=True)            
            return Response(serializer.data, status=status.HTTP_201_CREATED)                       
            # data = {                    
            #     "wallet_data": serializer.data,   
            # }

class CryptoCurrenciesList (GenericAPIView):
    def get(self, request):
        currencies= ('Bitcoin', 'Etherium', 'Litecoin','Cardano', 'Polkadot','Stellar')
        data= {
            "currencies" : currencies,
        }        
        return JsonResponse(data) 
            

                    

        
