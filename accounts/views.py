from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Favourite

# Create your views here.

def add_to_favourite(request, pk):
    product = get_object_or_404(Product, id = pk)
    fav_product = Favourite.objects.create(product = product)
    fav_product.save()
    return redirect('/')