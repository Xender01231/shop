from .models import Product
from django.shortcuts import render

# Create your views here.

def catalog(request):
    all_products = Product.objects.all() 
    return render(request, 'shop/catalog.html', {'all_products': all_products})

def create_order(request):
    return render(request, 'shop/create_order.html')

def orders(request):
    return render(request, 'shop/order.html')