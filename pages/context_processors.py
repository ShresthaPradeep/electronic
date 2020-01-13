from django.contrib.auth.decorators import login_required
from products.models import Category, Brand, Type, Feature, Product
from pages.models import Contact
from accounts.models import CartProduct


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

@login_required
def after_login_context(request):

    cart_products = CartProduct.objects.filter(user = request.user)
    return {
        "cart_products": cart_products,
    }