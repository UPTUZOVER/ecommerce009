from django.shortcuts import render
from .models import *
def store(request, category_slug=None):
    categories = None
    products = None

    products = Product.objects.all().filter(is_available=True)
    product_count = products.count()
    context = {
        "products": products,
        'product_count': product_count
    }
    return render(request,'store/store.html', context)





