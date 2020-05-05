from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.contrib.auth.models import User
from .models import orderForm


@login_required
def create_order(request):
    if request.method == 'POST':
        order = orderForm()
        order.paintlevel = request.POST['paintlevel']
        order.paintnum = request.POST['paintnum']
        order.build = request.POST['build']
        order.base = request.POST['base']
        order.comments = request.POST['comments']
        order.basetype = request.POST['basetype']
        order.scheme = request.POST['scheme']
        order.adnum = request.POST['adnum']
        order.adfirstline = request.POST['adfirstline']
        order.adtown = request.POST['adtown']
        order.adpostcode = request.POST['adpostcode']
        order.status = request.POST['status']
        order.user = request.user
        order.save()
        return render(request, 'order/createorder.html')
    else:
        return render(request, 'order/createorder.html')
    

def calculate_total(request):
    costs = {"Basic": 3,
         "Table Top": 6,
         "Display": 10,
         "False": 0,
         "True": 2,
         }