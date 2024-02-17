from shop.models import Product, Order
from django.shortcuts import render, redirect


def catalog(request):
    all_products = Product.objects.all() 
    return render(request, 'shop/catalog.html', {'all_products': all_products})

def create_order(request, id):
    print(request.GET)
    if request.method == 'POST':
        Order.objects.create(
            product_id = id,
            delivery_address = request.POST['delivery_address']
        )
        return redirect('orders')

    product = Product.objects.get(id=id)
    return render(request, 'shop/create_order.html', {'product': product})

def orders(request):
    orders = Order.objects.all() 
    return render(request, 'shop/orders.html', {'all_orders': orders })

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/product_detail.html', {'product': product})



