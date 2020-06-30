from django.db import models
from django.utils import timezone
from stdimage import StdImageField, JPEGField
from django.contrib.auth.models import User

class Products (models.Model):
    name = models.CharField(max_length=30)
    img = StdImageField(upload_to='images/',
                          variations={'resized': {'width': 250, 'height': 250 , "crop": True}, 'large': {'width': 600, 'height': 600}})
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
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

