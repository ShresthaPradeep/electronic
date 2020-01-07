from django.urls import path
from . import views

urlpatterns = [
    path('add_to_favourite/<int:pk>', views.add_to_favourite, name='add_to_favourite'),
]