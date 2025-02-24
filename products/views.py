from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

def home(request):
    products = Product.objects.all()  # Tüm ürünleri getir
    return render(request, 'home.html', {'products': products})


