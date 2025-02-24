from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from .models import CustomUser
import re  # Regex için import

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(
        label='Telefon Numarası',
        widget=forms.TextInput(attrs={'type': 'tel'}),
        max_length=11,  # En fazla 11 karakter olmalı
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'address')
        labels = {
            'username': 'Kullanıcı Adı',
            'email': 'E-posta Adresi',
            'address': 'Adres',
        }
        help_texts = {
            'username': 'Kullanıcı adı benzersiz olmalıdır.',
            'email': 'Geçerli bir e-posta adresi girin.',
            'phone_number': 'Telefon numarasını doğru formatta giriniz.',
            'address': 'Adresinizi buraya giriniz.',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # E-posta doğrulama
        try:
            EmailValidator()(email)
        except ValidationError:
            raise ValidationError("Geçerli bir e-posta adresi girin.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        
        # Telefon numarasının sadece rakamlardan oluştuğuna emin olalım
        if not re.match(r'^\d{11}$', phone_number):
            raise ValidationError('Telefon numarası yalnızca 11 rakamdan oluşabilir.')
        
        return phone_number

    # Password1 ve Password2 için açıklamalar ekleyelim
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Şifre'}),
        label='Şifre',
        help_text='Şifreniz en az 8 karakter olmalıdır ve kolayca tahmin edilememelidir.',
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Şifreyi Tekrar Girin'}),
        label='Şifreyi Tekrar Girin',
        help_text='Şifrenin doğruluğunu kontrol etmek için şifrenizi tekrar girin.',
    )
