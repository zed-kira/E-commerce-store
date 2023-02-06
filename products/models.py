from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self' , blank=True, null=True , related_name='children', on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        unique_together = ('slug', 'parent',) 
        verbose_name_plural = "categories"

    def __str__(self):                       
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Brand(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=00.00)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.ForeignKey('Category', null=True , blank=False, on_delete=models.CASCADE,
     related_name='categories',
    )
    brand = models.ForeignKey('Brand', null=True, blank=True,
        related_name = 'products' , on_delete=models.CASCADE)
    objects = models.Manager()
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

#class AbstractBrand(Brand):
 #   products_count = Product.objects.filter(brand=Brand.name)


