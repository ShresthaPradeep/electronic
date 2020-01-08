from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('add_to_favourite/<int:pk>', views.add_to_favourite, name='add_to_favourite'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]