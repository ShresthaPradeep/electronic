from django import template

register = template.Library()

from accounts.models import Favourite

@register.filter
def favourites(prod, pk):
    fav = Favourite.objects.filter(product = prod, user_id = pk)
    if fav.exists():
        return True
    else:
        return False