from django.urls import path
from .views import Checkout
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('checkout/', Checkout.as_view(), name="checkout")
]
