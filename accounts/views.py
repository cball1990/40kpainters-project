from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from .models import News
from products.models import Products
from checkout.models import OrderLineItem
from checkout.models import Order

def home(request):
    new = News.objects
    return render(request, 'accounts/home.html', {"news":new})

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request, 'accounts/signup.html', {'error':'Email Address Already exists'})
            
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['email'], password=request.POST['password1'], email=request.POST['email'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords do not match'})
    else:        
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Username or Password does not match'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

@login_required
def account(request,):
    User = request.user
    orders = Order.objects.all().order_by('-date')
    if User.username == 'admin':
        return render(request, 'accounts/adminaccount.html', {'order':orders})
    else:
        orders = Order.objects.filter(user=request.user)
        return render(request, 'accounts/account.html', {'order':orders}
        )

@login_required
def updatestatus(request, Order_id):
    orders = Order.objects.all().order_by('-date')
    if request.method == 'POST':
        updateorder = get_object_or_404(Order, pk=Order_id)
        updateorder.status = request.POST['status']
        updateorder.save()
        return render(request, 'accounts/adminaccount.html', {'order':orders})

@login_required
def addnewsitem(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['image']:
            news = News()
            news.title = request.POST['title']
            news.pub_date = timezone.datetime.now()
            news.body = request.POST['body']
            news.image = request.FILES['image']
            news.save()
            return redirect('account')
        else:
            return render(request,'accounts/adminaccount.html', {'error':'All Fields Are Required'})
    else:
        return render(request, 'accounts/addnews.html')    