from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['shipping_address']
        
  

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['shipping_address'].widget.attrs.update({'placeholder': 'Adresinizi girin'})