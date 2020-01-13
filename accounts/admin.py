from django.contrib import admin
from .models import Favourite, WaitList, Cart, CartProduct, UserProfile

admin.site.register(Favourite)
admin.site.register(WaitList)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(UserProfile)