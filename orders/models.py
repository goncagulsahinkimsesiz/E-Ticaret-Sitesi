from django.db import models
from users.models import CustomUser
from products.models import Product
from django.utils import timezone

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('shipped', 'Shipped')])
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

