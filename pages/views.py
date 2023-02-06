from django.shortcuts import render
from django.views.generic import TemplateView
from products.views import product_List

# Create your views here.

class HomePageView(product_List):
    template_name = "home.html"

class BlogPageView(TemplateView):
    template_name = "blog.html"

class ErrorPageView(TemplateView):
    template_name = "404.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"