from django.contrib import admin
from .models import Favourite, WaitList, Cart

admin.site.register(Favourite)
admin.site.register(WaitList)
admin.site.register(Cart)