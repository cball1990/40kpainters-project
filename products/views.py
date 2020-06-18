from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Products, ProductItem, Order

def productpage(request):
    context = {
        'products': Products.objects.all()
    }
    return render(request, 'products/products.html', context)

def productdetail(request, Products_id):
    product = get_object_or_404(Products, pk=Products_id)
    return render(request, 'products/detail.html', {'product':product})

def add_to_cart(request, Products_id):
    item = get_object_or_404(Products, pk=Products_id)
    order_item = ProductItem.objects.create(product=item)
    orderdate = timezone.now()
    order = Order.objects.create(user=request.user, orderdate=orderdate)
    order.items.add(order_item)
    return redirect("products")
