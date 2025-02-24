from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Cart, CartItem
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages  # messages framework'ünü içeri aktar

class CartDetailView(LoginRequiredMixin, View):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Sepetteki her bir ürünle ilgili detayları al
        cart_items = CartItem.objects.filter(cart=cart)

        # Sepet toplam fiyatını hesapla
        total_price = sum(item.product.price * item.quantity for item in cart_items)  # Sepet toplamı
        
        return render(request, 'cart/cart_detail.html', {'cart': cart, 'cart_items': cart_items, 'total_price': total_price})

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Sepetteki ürünü bul veya yeni ürün ekle
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        # Ürün zaten sepette varsa, miktarı arttır
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        # Sepete ekleme işlemi başarılı olduğunda mesaj gönder
        messages.success(request, f'{product.name} sepete eklendi.')

        return redirect('product_list')  # Ürünler sayfasına yönlendir
    




class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
        cart_item.delete()

       
        return redirect('cart_detail')
    
class DecreaseQuantityView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)

        # Ürün miktarını 1 azalt
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            messages.success(request, f'{cart_item.product.name} miktarı bir azaltıldı.')
        else:
            # Miktar 1 olduğunda, ürünü sepetten kaldır
            cart_item.delete()
            messages.success(request, f'{cart_item.product.name} sepetten çıkarıldı.')

        return redirect('cart_detail')  # Sepet detay sayfasına yönlendir
    

class IncreaseQuantityView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)

        # Sepetteki ürünün miktarını 1 artır
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'{cart_item.product.name} miktarı bir arttırıldı.')
        return redirect('cart_detail')  # Sepet sayfasına geri yönlendir

