from products.models import Category, Brand, Type, Feature, Product
from pages.models import Contact

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