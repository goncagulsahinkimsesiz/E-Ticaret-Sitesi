from django.urls import path
from .views import OrderListView, OrderDetailView, CreateOrderView
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order_list'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('create/', views.CreateOrderView.as_view(), name='create_order'),
]
