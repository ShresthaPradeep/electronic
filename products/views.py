from django.shortcuts import render, get_object_or_404
from django.views import generic

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Product, Brand, Feature, Category
from accounts.models import Favourite

# Create your views here.

def product_view(request, pk):
    product = get_object_or_404(Product, id = pk)
    product.view_count = product.view_count + 1
    product.save()
    
    context = {
        'product_detail': product,
    }
    return render(request, 'products/product_detail.html', context)


# class ProductDetailView(generic.DetailView):
#     context_object_name = 'product_detail'
#     model = Product
#     template_name = 'products/product_detail.html'


class BrandListView(generic.ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'products/products_list.html'
    paginate_by = 20

    def get_queryset(self):
        queryset = Product.objects.filter(brand_id = self.kwargs.get('pk'))
        return queryset
    
class FeatureListView(generic.ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'products/products_list.html'
    paginate_by = 20

    def get_queryset(self):
        queryset = Product.objects.filter(feature_id = self.kwargs.get('pk'))
        return queryset
        


class CategoryListView(generic.ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'products/products_list.html'
    paginate_by = 20

    def get_queryset(self):
        queryset = Product.objects.filter(category_id = self.kwargs.get('pk'))
        return queryset
        

class RelatedListView(generic.ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'products/products_list.html'
    paginate_by = 20

    def get_queryset(self):
        queryset = Product.objects.filter(brand_id = self.kwargs.get('pk'))
        return queryset
    


class MostViewedListView(generic.ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'products/products_list.html'
    paginate_by = 20

    def get_queryset(self):
        queryset = Product.objects.filter(view_count__gte =1).order_by('-view_count')
        
        return queryset