from django.db import models
from .userControl import UserControl
from .tipoQr import TipoQr
from app_qr.validator.validators import validate_texto_length, validate_descripcion_length
import uuid

class Qr(UserControl):
    tipo = models.ForeignKey(TipoQr, on_delete=models.DO_NOTHING, validators=[validate_texto_length])
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    texto = models.TextField(max_length=200)
    descripcion = models.TextField(max_length=200, validators=[validate_descripcion_length])
    is_active = models.BooleanField(default=True)
    base_url = models.URLField(editable=False)
    cantidad = models.IntegerField(editable=False, default=0)
    codigo = models.TextField(editable=False)

    def save(self, *args, **kwargs):
        self.base_url = f"http://localhost:8000/api/verificar/qr/{self.codigo}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.descripcion