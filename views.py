from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *


# Create your views here.
class SigninView(FormView):
    template_name = "adminsignin.html"
    form_class = SigninForm
    success_url = reverse_lazy('electronicapp:home')

 


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('electronicapp:home')




class HomeView(TemplateView):
	template_name = "home.html"