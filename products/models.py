from django.db import models
from django.utils import timezone
from stdimage import StdImageField, JPEGField
from django.contrib.auth.models import User

class Products (models.Model):
    name = models.CharField(max_length=30)
    img = StdImageField(upload_to='images/',
                          variations={'resized': {'width': 250, 'height': 250 , "crop": True}})
    description = models.CharField(max_length=500)
    price = models.FloatField()
    def __str__(self):
        return str(self.name)


class ProductItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
   


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(ProductItem)
    orderdate = models.DateTimeField(default=timezone.now)
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)

