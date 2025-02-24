from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        """ Admin kullanıcı adını yanlışlıkla silmeyi engelle """
        if obj and obj.username == "admin":  # Eğer kullanıcı adı "admin" ise silme engellensin
            return False
        return super().has_delete_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        """ Admin kullanıcı adını değiştirmeyi engelle """
        if obj and obj.username == "admin":  # Eğer kullanıcı adı "admin" ise değiştirme engellensin
            return False
        return super().has_change_permission(request, obj)

admin.site.register(CustomUser, CustomUserAdmin)
