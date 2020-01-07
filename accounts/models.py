from django.db import models
from products.models import Product

class Favourite(models.Model):
    product = models.ForeignKey(Product, on_delete = models.DO_NOTHING, blank = True, related_name='favourite_product')

    def __str__(self):
        return str(self.product)

class WaitList(models.Model):
    product = models.ForeignKey(Product, on_delete = models.DO_NOTHING, null = True, blank = True)
    

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete = models.DO_NOTHING, null = True, blank = True)

