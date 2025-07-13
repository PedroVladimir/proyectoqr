from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import verificar_qr
from .views_api import QrViewSet, TipoQrViewSet, QrActivosListView, ActivarDesactivarQR

router = DefaultRouter()
router.register(r'qrs', QrViewSet)
router.register(r'tipoqrs', TipoQrViewSet)


urlpatterns = [
    path('verificar/qr/<uuid:codigo_qr>/', verificar_qr, name='verificar-qr'),
    path('qr/<uuid:codigo_qr>/activar-desactivar/', ActivarDesactivarQR.as_view(), name='activar-desactivar-qr'),
    path('', include(router.urls)),
    path('qrs-activos/', QrActivosListView.as_view(), name='qrs-activos'),
]