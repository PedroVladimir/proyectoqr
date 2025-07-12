from django.db import models
from .validator.validators import validate_texto_length
import uuid

# MODELO TIPO QR
# URL, TEXTO, LUGAR 
class TipoQr(models.Model):
    tipo = models.TextField(max_length=100, validators=[validate_texto_length])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo

#MODELO QR
class Qr(models.Model):
    tipo = models.ForeignKey(TipoQr, on_delete=models.DO_NOTHING)
    codigo = models.UUIDField(editable=False, unique=True)
    texto = models.TextField(max_length=200)
    descripcion = models.TextField(max_length=200)
    is_active = models.BooleanField(default=True)
    base_url = models.URLField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.codigo:  
            self.codigo = uuid.uuid4() 
        self.base_url = f"http://localhost:8000/api/verificar/qr/{self.codigo}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.descripcion

#MODELO PARA REGISTRAR DISPOSITIVO
class EscanearQr(models.Model):
    qr = models.ForeignKey(Qr, on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    dispositivo = models.JSONField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.qr.descripcion

