from django.db import models
from products.models import Products
from django.contrib.auth.models import User

Status_Choices= (
    ('ordered','Ordered'),
    ('paid','Paid'),
    ('painted','Painting Complete'),
    ('basing','Basing Complete'),
    ('finishing','Final Touches'),
    ('complete','Waiting To Be Shipped'),
    ('shipped','Shipped')
)

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, related_name="orderline")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=Status_Choices, default='ordered')

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)

