import jwt
from rest_framework.authentication import BaseAuthentication #This authentication scheme uses HTTP Basic Authentication
from rest_framework import exceptions
from django.conf import settings
from authentication.models import UserCrypto

# Note: If you use BasicAuthentication in production you must ensure that your API is only available over https. 
# You should also ensure that your API clients will always re-request the username and password at login, 
# and will never store those details to persistent storage.


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        #Get the access token based on a request.
        #Returns None if no authentication details were provided. Raises
        #AuthenticationFailed if the token is incorrect.
        if not auth_data:
            return None

        prefix, token = auth_data.decode('utf-8').split(' ')
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)

            user = UserCrypto.objects.get(email=payload['email'])
            return (user, token)

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Your token is invalid,login')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('Your token is expired,login')

        return super().authenticate(request)