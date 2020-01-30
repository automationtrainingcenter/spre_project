from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            print('invalid credentials')
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            print('username already taken')
            messages.error(request, 'Username already taken')
        else:
            if password:
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                         email=email, password=password)
            return redirect('login')
    return render(request, 'accounts/register.html')


def logout_view(request):
    return render(request, 'accounts/logout.html')


def dashboard(request):
    return render(request, 'account/dashboard.html')
