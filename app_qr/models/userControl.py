from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserControl(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="actualizado")
    user_create = models.ForeignKey(User, related_name='%(class)s_creados', on_delete=models.SET_NULL, null=True, editable=False)
    user_update = models.ForeignKey(User, related_name='%(class)s_actualizados', on_delete=models.SET_NULL, null=True, editable=False)
    
    class Meta:
        abstract = True
    