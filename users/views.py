# users/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm  # Kendi özelleştirilmiş formu ekliyoruz
from django.shortcuts import render, redirect
from django.contrib import messages

# Kullanıcı kayıt işlemi
class UserRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm  # Özelleştirilmiş formu kullanıyoruz
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')  # Başarılı kayıt sonrası login sayfasına yönlendirme

# Kullanıcı giriş işlemi
class UserLoginView(LoginView):
    template_name = 'users/login.html'  # Giriş için özelleştirilmiş şablon
    success_url = reverse_lazy('home')  # Kullanıcı giriş yaptıktan sonra yönlendirileceği sayfa
    
    def form_valid(self, form):
        # Admin'e giriş engelleniyor
        user = form.get_user()
        if user.is_superuser:
            messages.error(self.request, 'Admin kullanıcıları normal kullanıcılara giriş yapamaz.')
            return redirect('login')  # Admin giriş yapmaya çalışırsa tekrar giriş sayfasına yönlendiriliyor.
        
        # Normal kullanıcı için işlemi devam ettir
        return super().form_valid(form)
    
# Kullanıcı çıkış işlemi
class UserLogoutView(LogoutView):
    next_page = '/users/login/'  # Çıkış sonrası login sayfasına yönlendirme
