from django.db import models
from category.models import Category

class Product(models.Model):
    product_name = models.CharField(max_length=444, unique=True)
    slug = models.SlugField(max_length=434, unique=True)
    description = models.TextField(blank=True, max_length=876)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField(default=0, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name










