from django.contrib import admin

from .models import Products, ProductItem, Order

admin.site.register(Products)
admin.site.register(ProductItem)
admin.site.register(Order)

