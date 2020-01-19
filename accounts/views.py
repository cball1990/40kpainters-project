from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.object.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username Already exists'})
            
            except:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords do not match'})
    else:        
        return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def account(request):
    return render(request, 'accounts/account.html')
