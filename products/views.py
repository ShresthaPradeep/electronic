from django.shortcuts import render, get_object_or_404
from django.views import generic

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Product, Brand, Feature, Category

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
    context_object_name = 'brands'
    queryset = Brand.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs.get('pk'))
    
class FeatureListView(generic.ListView):
    context_object_name = 'features'
    queryset = Feature.objects.all()
    template_name = 'products/features_list.html'
    
    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs.get('pk'))


class CategoryListView(generic.ListView):
    context_object_name = 'category'
    queryset = Category.objects.all()
    paginate_by = '4'
    
    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs.get('pk'))


class RelatedListView(generic.ListView):
    context_object_name = 'related'
    queryset = Product.objects.all()
    template_name = 'products/related_list.html'
    
    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs.get('pk'))


class MostViewedListView(generic.ListView):
    context_object_name = 'most_viewed'
    model = Product
    template_name = 'products/most_viewed.html'

    def get_queryset(self):
        queryset = Product.objects.filter(view_count__gte =1).order_by('-view_count')
        
        return queryset