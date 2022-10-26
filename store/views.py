from django.shortcuts import render
from .models import Product
from category.models import Category
# Create your views here.

def store(request, category_slug=None):
    categories = None
    products =None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    products = Product.objects.all().filter(is_available=True)
    product_count = products.count()


    context = {
        'products': products,
        'product_count' : products.count()
    }
    return render(request, 'store/store.html', context)
