from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('search', views.search, name='search'),
    path('subscribe', views.subscribe, name='subscribe'),
]