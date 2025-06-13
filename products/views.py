from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list_view(request):
    products = Product.objects.prefetch_related('images').select_related('category')
    return render(request, 'products/product_list.html', {'products': products})


def product_detail_view(request, slug):
    product = get_object_or_404(Product.objects.prefetch_related('images'), slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})