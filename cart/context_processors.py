from .models import CartItem, Cart

def cart_len(request):

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        if not created:
            items = CartItem.objects.filter(cart=cart)
            length = len(items)
        else:
            items = {}
            length = len(items)
    else:
        items = {}
        length = len(items)
    return {'items' : items , 'items_len': length}

