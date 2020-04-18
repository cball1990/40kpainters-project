from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.contrib.auth.models import User
from .forms import orderform
from .models import order_form


@login_required
def create_order(request):
    form = orderform(request.POST or None)
    if form.is_valid():
        form.save()
    
        return redirect('order/payment.html')
    else:
        context ={
            'form':form }
        return render(request, 'order/createorder.html', context)

def calculate_total(request):
    costs = {"Basic": 3,
         "Table Top": 6,
         "Display": 10,
         "False": 0,
         "True": 2,
         }