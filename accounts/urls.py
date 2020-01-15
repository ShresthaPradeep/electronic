from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('favourite', views.FavouriteView.as_view(), name='favourite'),
    path('add_to_favourite/<int:pk>', views.add_to_favourite, name='add_to_favourite'),
    path('add_to_cart_from_favourite/<int:pk>', views.add_to_cart_from_favourite, name='add_to_cart_from_favourite'),
    path('remove_from_favourite/<int:pk>', views.remove_from_favourite, name='remove_from_favourite'),
    path('wait', views.WaitView.as_view(), name='wait'),
    path('add_to_wait/<int:pk>', views.add_to_wait, name='add_to_wait'),
    path('add_to_cart_from_wait/<int:pk>', views.add_to_cart_from_wait, name='add_to_cart_from_wait'),
    path('remove_from_wait/<int:pk>', views.remove_from_wait, name='remove_from_wait'),
    path('add_to_cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('edit_cart', views.edit_cart, name='edit_cart'),
    path('remove_from_cart/<int:pk>', views.remove_from_cart, name='remove_from_cart'),
    path('cart', views.CartView.as_view(), name='cart'),
    path('notification', views.NotificationView.as_view(), name='notification'),
    path('order', views.OrderView.as_view(), name='order'),
    path('add_to_order/<int:pk>', views.add_to_order, name='add_to_order'),
]