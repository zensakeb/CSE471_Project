from django.shortcuts import render

# Create your views here.
# almari/products/views.py

from django.shortcuts import render

def product_list(request):
    # `products/list.html` should be your template for listing products
    return render(request, 'products/list.html', {
        'products': [],  # replace with real queryset later
    })