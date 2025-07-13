from rest_framework import viewsets, generics
from .models.qr import Qr
from .models.tipoQr import TipoQr
from .serializers import QrSerializer, TipoQrSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# VIEWSET PARA EL MODELO QR
# http://localhost:8000/api/qrs/
class QrViewSet(viewsets.ModelViewSet):
    queryset = Qr.objects.all()
    serializer_class = QrSerializer

# VIEWSET PARA EL MODELO TIPOQR
# http://localhost:8000/api/tipoqrs/
class TipoQrViewSet(viewsets.ModelViewSet):
    queryset = TipoQr.objects.all()
    serializer_class = TipoQrSerializer

# LISTVIEW DE QR ACTIVOS
# http://localhost:8000/api/qrs-activos/
class QrActivosListView(ListAPIView):
    serializer_class = QrSerializer
    def get_queryset(self):
        return Qr.objects.filter(is_active=True)
    
# ACTIVA DESACTIVAR UN QR 
# http://localhost:8000/api/qr/fecb2d64-d5eb-467c-a256-3fbc2867bb52/activar-desactivar/
# BODY { "is_active" : 0 } 1 = ACTIVO, 0 = INACTIVO
class ActivarDesactivarQR(APIView):
    def post(self, request, codigo_qr):
        qr = Qr.objects.get(codigo=codigo_qr)
        qr.is_active = request.data.get('is_active', qr.is_active)
        qr.save()

        return Response("completado")
    