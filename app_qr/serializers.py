from rest_framework import serializers
from .models.qr import Qr
from .models.tipoQr import TipoQr

class QrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qr
        fields = '__all__'

class TipoQrSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoQr
        fields = '__all__'