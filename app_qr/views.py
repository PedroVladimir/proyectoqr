from django.shortcuts import render, get_object_or_404, redirect
from app_qr.models import Qr, EscanearQr

def verificar_qr(request, codigo_qr):
    qr = get_object_or_404(Qr, codigo = codigo_qr, is_active = True)
    #contar el scaneo del codigo
    qr.incrementar_contador()
        
    # Registrar el escaneo 
    EscanearQr.objects.create(
        qr=qr,
        ip_address=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT', '')
    )
    
    # Redireccionar a la URL del QR
    return redirect(qr.texto)