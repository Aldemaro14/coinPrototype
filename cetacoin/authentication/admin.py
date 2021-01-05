from django.contrib import admin
from authentication.models import *

# Register your models here.

class UserCryptoAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name' , 'email', 'password')
admin.site.register(UserCrypto, UserCryptoAdmin)