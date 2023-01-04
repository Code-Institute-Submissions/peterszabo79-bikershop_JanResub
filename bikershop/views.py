from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)

def handler400(request, exception):
    """ Error Handler 400 - Bad Request """
    return render(request, 'errors/400.html', status=400)

def handler403(request, exception):
    """ Error Handler 403 - Page Not Found """
    return render(request, 'errors/403.html', status=403)


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, 'errors/404.html', status=404)


def handler405(request):
    """ Error Handler 405 - Method Not Allowed """
    return render(request, 'errors/405.html', status=405)


def handler500(request):
    """ Error Handler 500 - Internal Server Error """
    return render(request, 'errors/500.html', status=500)