#Create your database models here.

from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=200)

class Customer(models.Model):
    firstName = models.CharField(max_length=200)
