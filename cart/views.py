from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import  TemplateView
from .models import CartItem, Cart
from products.models import Product
import json
from .context_processors import cart_len

# Create your views here.

def cart(request):
    context = cart_len(request)
    return render(request, 'cart.html', context)

#request is sent from cart.js to update_cart
def update_cart(request):

    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']

    product = Product.objects.get(id=productID)
    cart, created_cart = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if action == 'add' and not created:
        cart_item.quantity = (cart_item.quantity + 1)
        cart_item.save()
    elif action == 'delete':
        cart_item.delete()
    
    elif action == 'quantity-up':
        cart_item.quantity += 1
        cart_item.save()
    elif action == 'quantity-down':
        cart_item.quantity -= 1
        if cart_item.quantity == 0:
            cart_item.delete()
        else:
            cart_item.save()
    price = cart_item.product.price * cart_item.quantity
    js_response = cart_len(request)
    
    return JsonResponse(str(js_response['items_len'])+' '+str(cart_item.quantity)+' '+str(price), safe=False)

class Checkout(TemplateView):
    template_name = "checkout.html"