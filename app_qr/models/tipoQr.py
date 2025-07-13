from django.db import models
from .userControl import UserControl
from app_qr.validator.validators import validate_texto_length, validate_descripcion_length

class TipoQr(UserControl):
    tipo = models.CharField(max_length=100, validators=[validate_texto_length])
    descripcion = models.TextField(max_length=200, validators=[validate_descripcion_length])

    def __str__(self):
        return self.tipo