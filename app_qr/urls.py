from django.urls import path
from .views import verificar_qr

urlpatterns = [
    path('verificar/qr/<uuid:codigo_qr>/', verificar_qr, name='verificar-qr'),
]