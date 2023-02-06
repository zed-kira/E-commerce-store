from django.urls import path
from .views import HomePageView, BlogPageView , ErrorPageView , ContactPageView
from cart.views import update_cart

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('404/', ErrorPageView.as_view(), name='error'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('update_cart/', update_cart , name="update_cart")
]
