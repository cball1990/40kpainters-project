from django.contrib import admin

from .models import Products, ProductItem, order

admin.site.register(Products)
admin.site.register(ProductItem)
admin.site.register(order)

