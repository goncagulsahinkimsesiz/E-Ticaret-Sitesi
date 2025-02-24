# users/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm  # Kendi özelleştirilmiş formu ekliyoruz

# Kullanıcı kayıt işlemi
class UserRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm  # Özelleştirilmiş formu kullanıyoruz
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')  # Başarılı kayıt sonrası login sayfasına yönlendirme

# Kullanıcı giriş işlemi
class UserLoginView(LoginView):
    template_name = 'users/login.html'  # Giriş için özelleştirilmiş şablon

# Kullanıcı çıkış işlemi
class UserLogoutView(LogoutView):
    next_page = '/users/login/'  # Çıkış sonrası login sayfasına yönlendirme
