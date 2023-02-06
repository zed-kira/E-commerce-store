from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    objects = models.Manager()

    def __str__(self):
        return "Cart id : {id}".format(id=self.pk)
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete= models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    objects = models.Manager()

    def get_total_price(self):
        return self.product.price * self.quantity


    class Meta:
        ordering = ['date_added']
