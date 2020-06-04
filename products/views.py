from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Products

def productpage(request):
    context = {
        'products': Products.objects.all()
    }
    return render(request, 'products/products.html', context)
