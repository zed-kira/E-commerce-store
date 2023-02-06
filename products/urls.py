from django.urls import path

from .models import Product
from .views import product_List

urlpatterns = [
    path('', product_List.as_view(), name='product_list'),
]
