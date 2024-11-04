from itertools import product
from django.shortcuts import *

from store.models import Product
from . import urls

def home(request):
    products = Product.objects.filter(is_available=True)
    context = {
        'products': products
    }
    return render(request, 'home.html', context)