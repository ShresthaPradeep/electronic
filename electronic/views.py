from django.shortcuts import render
from accounts.models import Favourite, CartProduct, WaitList, Notification
from django.http import JsonResponse
import json

def favourites(request):
    favourites = Favourite.objects.filter(user = request.user).values('product_id', 'product__name', 'product__thumbnail_main', 'product__selling_price')
    return JsonResponse({ 'favourites': list(favourites) })

def carts(request):
    carts = CartProduct.objects.filter(user = request.user, checked_out = False).values('product_id', 'product__name', 'product__thumbnail_main', 'product__selling_price')
    return JsonResponse({ 'carts': list(carts) })

def waits(request):
    waits = WaitList.objects.filter(user = request.user).values('product_id', 'product__name', 'product__thumbnail_main', 'product__selling_price')
    return JsonResponse({ 'waits': list(waits) })

def notifications(request):
    notifications = Notification.objects.filter(user = request.user).values('title', 'message')
    return JsonResponse({ 'notifications': list(notifications) })
