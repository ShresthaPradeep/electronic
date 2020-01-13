from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from pages.models import Banner, Subscriber
from products.models import Brand, Feature, Product

from .forms import SubscriberForm

# Create your views here.
class Index(generic.TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['banners'] = Banner.objects.all()
        context['brands'] = Brand.objects.all()
        context['features'] = Feature.objects.all()
        context['products'] = Product.objects.all()
        context['most_viewed'] = Product.objects.filter(view_count__gte =1).order_by('-view_count')
        return context


def search(request):
    queryset_list = Product.objects.all()

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords == '':
            queryset_list = queryset_list.filter(name__iexact=keywords)
            return render(request, 'pages/search.html', {'results': queryset_list})

        else:
            queryset_list = queryset_list.filter(name__icontains=keywords) | queryset_list.filter(description__icontains=keywords)
            return render(request, 'pages/search.html', {'results': queryset_list})


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST or None)

        if form.is_valid():
            subscriber_email_qs = Subscriber.objects.filter(subscriber_email = form.instance.subscriber_email)
            if subscriber_email_qs.exists():
                messages.info(request, ('You are already subscribed'))
                return redirect('index')
            else:
                form.save() 
                messages.info(request, ('You have subscribed'))
                return redirect('index')
