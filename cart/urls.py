from django.urls import path
from .views import CartDetailView, AddToCartView, RemoveFromCartView, DecreaseQuantityView, IncreaseQuantityView

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('decrease/<int:product_id>/', DecreaseQuantityView.as_view(), name='decrease_quantity'),
    path('increase/<int:product_id>/', IncreaseQuantityView.as_view(), name='increase_quantity'),






]


