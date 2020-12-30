from django.db import models

# Create your models here.

class UserCrypto(models.Model):
    firstName = models.CharField(max_length=254, min_length=5)
    lastName = models.CharField(max_length=254, min_length=5)
    email = models.EmailField(max_length=254, **options)
    password = models.CharField(max_length=65, min_length=8)

class Wallet(models.Model):
    id = models.Integer(**options)
    amount = models.DecimalField(max_digits=12, decimal_places=5)
    currency = models.CharField(max_length=15)
    test = models.CharField(max_length=122)
