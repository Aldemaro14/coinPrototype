from rest_framework import serializers
from authentication.models import UserCrypto, Wallet, MinerCrypto
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Override validate to return more user attributes
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['email'] = self.user.email
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        #list all the wallets for the user
        user=UserCrypto.objects.get(email= self.user.email)
        wallets = Wallet.objects.filter(user=user.id)
        serializer = WalletSerializer(wallets, many=True)
        data['wallets']= serializer.data
        return data

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)        
        return token
  


class UserSerializer(serializers.ModelSerializer):
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

class MinerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinerCrypto
        fields = ['username']
    
    def validate(self, attrs):
        username = attrs.get('username','')
        if MinerCrypto.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)
    

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=2)

    class Meta:
        model = UserCrypto
        fields = ['email', 'password']


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['idWallet', 'amount', 'currency',
                  'alias', 'user', 'miner']
