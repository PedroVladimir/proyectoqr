from django.db import models
from django.db.models import F
from .userControl import UserControl
from .tipoQr import TipoQr
from app_qr.validator.validators import validate_texto_length, validate_descripcion_length
from io import BytesIO
import uuid
import base64
import qrcode

class Qr(UserControl):
    tipo = models.ForeignKey(TipoQr, on_delete=models.DO_NOTHING)
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    texto = models.TextField(max_length=200, validators=[validate_texto_length])
    descripcion = models.TextField(max_length=200, validators=[validate_descripcion_length])
    is_active = models.BooleanField(default=True)
    base_url = models.URLField(editable=False)
    cantidad = models.IntegerField(editable=False, default=0)
    codigo_base64 = models.TextField(editable=False)

    def save(self, *args, **kwargs):
        self.base_url = f"http://localhost:8000/api/verificar/qr/{self.codigo}"

        if not self.codigo_base64:
            self.generar_codigo_qr()
        
        super().save(*args, **kwargs)
    
    def generar_codigo_qr(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.base_url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        self.codigo_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
    
    def incrementar_contador(self):
        Qr.objects.filter(pk=self.pk).update(cantidad=F('cantidad') + 1)
        self.refresh_from_db()
    
    def __str__(self):
        return self.descripcion