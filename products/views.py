from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Products

@login_required
def productpage(request):
    context = {
        'products': Products.objects.all()
    }
    return render(request, 'products/products.html', context)

def productdetail(request, Products_id):
    product = get_object_or_404(Products, pk=Products_id)
    return render(request, 'products/detail.html', {'product':product})

