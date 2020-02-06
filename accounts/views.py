from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from pages.views import index
from contacts.models import contact
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome to Dashboard')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('password2')
        if password == conf_password:
            if User.objects.filter(username=username).exists():
                print('username already taken')
                messages.error(request, 'Username already taken')
            else:
                if password:
                    User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                             email=email, password=password)
                return redirect('login')
        else:
            messages.error(request, 'Passwords did not match')
    return render(request, 'accounts/register.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'logged out successfully')
    return redirect(index)


def dashboard(request):
    contacts = contact.objects.order_by('-contact_date')
    context = {
        'contacts': contacts
    }
    return render(request, 'accounts/dashboard.html', context)
