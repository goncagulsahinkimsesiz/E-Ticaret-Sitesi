from django.shortcuts import render
from .models import Product  # Ürün modelini içe aktar

def home(request):
    products = Product.objects.all()  # Tüm ürünleri çek
    return render(request, 'base.html', {'products': products})


