from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    is_featured = models.BooleanField(default=False)  # Ana sayfada gösterilecek mi?

    def __str__(self):
        return self.name
