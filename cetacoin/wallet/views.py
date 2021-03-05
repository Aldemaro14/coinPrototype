from django.shortcuts import render
from authentication.models import UserCrypto, Wallet
from authentication import params
#Account creation for algorant network
from algosdk import account, encoding, mnemonic, algod
# Create your views here.


class WalletCreationView(GenericAPIView):    
    wallet_serializer = WalletSerializer(data=wallet_dict)
    def post(self, request):
        with transaction.atomic():
            print(request)
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
            serializer = WalletSerializer(data= wallet_dict)
            if wallet_serializer.is_valid():
                        # Saving wallet object associated for the user
                wallet_serializer.save()
                data = {                    
                    "wallet_data": wallet_serializer.data,
                    #"wallet_bitcoinb": w.as_json(),
                    "wallet_bitcoinb":acl.account_info(address),
                }
                return Response(data, status=status.HTTP_201_CREATED)
            # deleting new user if the default wallet could not be createad
            #wallets.wallet_delete_if_exists("Wallet" + str(new_user.id)+"BTC")
            new_user.delete()
            return Response(wallet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class WalletListView(GenericAPIView):    
    wallet_serializer = WalletSerializer(data=wallet_dict)
    def get(self, request):        
            print(request)            
            user=UserCrypto.objects.get(email= request.data['email'])
            wallets = Wallet.objects.filter(user=user)
            serializer = WalletSerializer(data= wallets, many=True)
            data = {                    
                "wallet_data": serializer.data,
                #"wallet_bitcoinb": w.as_json(),
                "wallet_bitcoinb":acl.account_info(address),
            }
            return Response(data)
            # deleting new user if the default wallet could not be createad
            #wallets.wallet_delete_if_exists("Wallet" + str(new_user.id)+"BTC")            

                    

        
