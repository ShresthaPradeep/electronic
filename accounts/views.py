from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from products.models import Product
from .models import Favourite
from .forms import RegistrationForm, LoginForm

# Create your views here.

def add_to_favourite(request, pk):
    product = get_object_or_404(Product, id = pk)
    fav_product = Favourite.objects.create(product = product)
    fav_product.save()
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']

        # Check Username
        if User.objects.filter(username = username).exists():
            messages.error(request, 'That username already exists')
            return redirect('register')
        else:
            if User.objects.filter(email = email).exists():
                messages.error(request, 'That email already exists')
                return redirect('register')
            else:
                user = User(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
            
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
    
    return redirect('index')