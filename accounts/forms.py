from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "name": "username",
        "class": "form-control",
    }), label="")
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "text",
        "name": "email",
        "class": "form-control",
    }), label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "type": "password",
        "name": "password",
        "class": "form-control",
    }), label="")

    class Meta:
        model = User
        fields = {'username','email', 'password'}



class LoginForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "text",
        "name": "email",
        "class": "form-control",
    }), label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "type": "password",
        "name": "password",
        "class": "form-control",
    }), label="")

    class Meta:
        model = User
        fields = {'username','email', 'password'}