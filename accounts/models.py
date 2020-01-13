from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from products.models import Product

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    username = models.CharField(max_length=200)
    photo = models.ImageField(upload_to = 'users/%Y/%m/%d/', blank = True, null = True, default='default_user.png')
    address = models.CharField(max_length=200, blank = True, null = True)
    email = models.EmailField(blank = True, null = True)
    phone = models.CharField(max_length=10, blank = True, null = True)
    ship_address1 = models.CharField(max_length=200, blank = True, null = True)
    ship_address2 = models.CharField(max_length=200, blank = True, null = True)
    ship_phone = models.CharField(max_length=10, blank = True, null = True)
    ship_email = models.EmailField(blank = True, null = True)

    def __str__(self):
        return self.user.username


class Favourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.DO_NOTHING, blank = True, related_name='favourite_product')

    def __str__(self):
        return str(self.product)

class WaitList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.DO_NOTHING, null = True, blank = True)

    def __str__(self):
        return self.product.name
    
class CartProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    color = models.CharField(max_length=150)
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name

    def total_price(self):
        return self.quantity * self.product.selling_price

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ManyToManyField(CartProduct)
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    building = models.CharField(max_length=200, null=True, blank = True)
    order_notes = models.TextField(max_length=300, null=True, blank = True)

    def __str__(self):
        return self.user.username