from django.shortcuts import render
from django.views.generic import ListView
from .models import Product , Category , Brand
# Create your views here.

class product_List(ListView):
    model = Product
    context_object_name = 'products_list'
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand_count = {}
        brands = Brand.objects.all()
        for brand in brands:
            count = brand.products.count()
            brand_count[brand.name] = count

        context['categories'] = Category.objects.all()
        context['brands'] = brand_count
        return context 
