from django.shortcuts import render
from django.views import generic
from pages.models import Banner
from products.models import Brand, Feature, Product

# Create your views here.
class Index(generic.TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['banners'] = Banner.objects.all()
        context['brands'] = Brand.objects.all()
        context['features'] = Feature.objects.all()
        context['products'] = Product.objects.all()
        return context


def search(request):
    queryset_list = Product.objects.all()

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(name__icontains=keywords) | queryset_list.filter(description__icontains=keywords)

    context = {
        'results': queryset_list,
    }

    return render(request, 'pages/search.html', context)