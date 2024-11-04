from django.shortcuts import render
from .models import Product

def store(request, catslug=None):
    if catslug != None:
        products = Product.objects.filter(category__slug=catslug)
    else:
        products = Product.objects.all()
    product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)

def product_details(request, catslug=None, product_slug=None):
    product = Product.objects.get(category__slug=catslug, slug=product_slug)
    context= {
        'single_product': product,
    }
    return render(request, 'store/product-details.html', context)

from django.shortcuts import render
from .models import Product

def search_products(request):
    query = request.GET.get('q')
    if query:
        # Search for products by name
        products = Product.objects.filter(product_name__icontains=query)
    else:
        products = Product.objects.all()
    
    context = {
        'products': products
    }
    return render(request, 'store/search_result.html', context)
