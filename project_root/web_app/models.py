#Create your database models here.

from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=200)
    productPrice = models.IntegerField()
    productBrand = models.CharField(max_length=200)
    productCategory = models.TextField()

    def __str__(self):
        return self.text