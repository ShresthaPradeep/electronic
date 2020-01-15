from django.contrib import admin
from .models import Favourite, WaitList, Cart, CartProduct, UserProfile, Notification, Order

admin.site.register(Favourite)
admin.site.register(WaitList)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(UserProfile)
admin.site.register(Notification)
admin.site.register(Order)