from django.contrib import admin
from .models import TipoQr, Qr

# Register your models here.
@admin.register(TipoQr)
class TipoQrAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')
    list_filter = ('tipo',)



@admin.register(Qr)
class QrAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'texto', 'descripcion', 'codigo', 'is_active')
    list_filter = ('tipo', 'is_active')
