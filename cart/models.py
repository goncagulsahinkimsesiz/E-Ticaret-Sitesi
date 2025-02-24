from django.db import models
from users.models import CustomUser
from products.models import Product

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def _str_(self):
        return f"Cart of {self.user.username}"
    
    @property   #toplam tutarı hesaplamak için yazıldı
    def total_price(self):
        total = sum(item.product.price * item.quantity for item in self.cartitem_set.all())
        return total

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cartitem_set', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def _str_(self):
        return f"{self.quantity} x {self.product.name} in cart"

