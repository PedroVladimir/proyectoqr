from django.db import models
from .userControl import UserControl
from .qr import Qr

class EscanearQr(UserControl):
    qr = models.ForeignKey(Qr, on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    dispositivo = models.JSONField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.qr.descripcion