from django.contrib.auth.decorators import login_required
from products.models import Category, Brand, Type, Feature, Product
from pages.models import Contact
from accounts.models import CartProduct, UserProfile, Favourite, WaitList, Notification


def global_context(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    brands = Brand.objects.all()
    types = Type.objects.all()
    contacts = Contact.objects.all()
    return {
        "categories": categories,
        "products": products,
        "brands": brands,
        "types": types,
        "contacts": contacts,
    }


def after_login_context(request):
    if request.user.is_authenticated:
        cart_products = CartProduct.objects.filter(user = request.user)
        profiles = UserProfile.objects.filter(user = request.user)
        favourites = Favourite.objects.filter(user = request.user)
        wish_products = WaitList.objects.filter(user = request.user)
        notifications = Notification.objects.filter(user = request.user)
        return {
            "favourites": favourites,
            "cart_products": cart_products,
            "wish_products": wish_products,
            "profiles": profiles,
            "notifications": notifications,
        }
    else:
        return ()