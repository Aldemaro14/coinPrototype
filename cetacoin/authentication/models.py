from django.db import models


# Create your models here.

class UserCrypto(models.Model):
    username = models.CharField(max_length=15)
    firstName = models.CharField(max_length=254)
    lastName = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=65)

class Wallet(models.Model):
    idWallet = models.IntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=5)
    currency = models.CharField(max_length=15)
    test = models.CharField(max_length=122)
