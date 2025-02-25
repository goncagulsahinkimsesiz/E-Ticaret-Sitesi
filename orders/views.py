from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from .forms import OrderForm  # forms.py içindeki OrderForm'u import et
from products.models import Product
from cart.models import Cart, CartItem
from django.core.exceptions import PermissionDenied



class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        # Kullanıcının sadece kendi siparişlerini getirmesini sağlıyoruz
        return Order.objects.filter(user=self.request.user)

class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

    def get_object(self):
        # Kullanıcının sadece kendi siparişinin detayına ulaşabilmesini sağlıyoruz
        order = super().get_object()
        if order.user != self.request.user:
            raise PermissionDenied  # Eğer sipariş sahibiyle giriş yapan kullanıcı uyuşmazsa hata verir
        return order

class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm  # fields yerine form_class kullanıyoruz
    template_name = 'orders/create_order.html'
    success_url = reverse_lazy('order_list')

    def get_initial(self):
        # Giriş yapmış kullanıcıyı otomatik ekle
        initial = super().get_initial()
        initial['user'] = self.request.user

        # Sepetteki ürünleri otomatik olarak siparişe ekle
        cart = get_object_or_404(Cart, user=self.request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        # Sepet ürünleri için toplam fiyatı hesapla
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        initial['total_price'] = total_price

        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Sepetteki ürünleri ve adetlerini template'e gönder
        cart = get_object_or_404(Cart, user=self.request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        
        # Toplam fiyatı hesapla ve context'e ekle
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        context['cart_items'] = cart_items
        context['total_price'] = total_price  
        
        return context

    def form_valid(self, form):
        order = form.save(commit=False)
        order.user = self.request.user

        # Kullanıcının sepetini al
        cart = Cart.objects.filter(user=self.request.user).first()
        if not cart:
            print("Sepet bulunamadı")
            return redirect('cart_view')

        cart_items = CartItem.objects.filter(cart=cart)
        if not cart_items.exists():
            print("Sepet boş")
            return redirect('cart_view')

        # Sunucu tarafında toplam fiyatı hesapla
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        order.total_price = total_price  # Formdan almak yerine burada hesaplıyoruz

        order.save()

        # ManyToMany için ürünleri ekleyelim
        order.products.set([item.product for item in cart_items])

        # Sipariş tamamlandığında sepeti temizle
        cart_items.delete()

        return redirect(self.success_url)
