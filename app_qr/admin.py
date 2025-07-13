from django.contrib import admin
from .models import TipoQr, Qr, EscanearQr

# Register your models here.
@admin.register(TipoQr)
class TipoQrAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')
    list_filter = ('tipo',)



@admin.register(Qr)
class QrAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'texto', 'descripcion', 'base_url', 'codigo_base64', 'is_active')
    list_filter = ('tipo', 'is_active')


@admin.register(EscanearQr)
class EscanearQrAdmin(admin.ModelAdmin):
    list_display = ('id', 'qr', 'fecha', 'ip_address', 'dispositivo', 'user_agent')
    list_filter = ('qr', 'ip_address', 'dispositivo', 'user_agent')