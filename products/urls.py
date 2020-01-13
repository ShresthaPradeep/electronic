from django.urls import path
from . import views

urlpatterns = [
    path('product_list/brands/<int:pk>', views.BrandListView.as_view(), name='brand_list'),
    path('product_list/features/<int:pk>', views.FeatureListView.as_view(), name='feature_list'),
    path('product_list/categories/<int:pk>', views.CategoryListView.as_view(), name='category_list'),
    path('product_list/related/<int:pk>', views.RelatedListView.as_view(), name='related_list'),
    path('product_list/most_viewed', views.MostViewedListView.as_view(), name='most_viewed'),
    path('<int:pk>', views.product_view, name='product_detail'),
]