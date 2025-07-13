from django.core.exceptions import ValidationError

def validate_texto_length(value):
    if not (4 <= len(value) <= 50):
        raise ValidationError('El texto debe tener entre 4 y 40 caracteres.')

def validate_descripcion_length(value):
    if not (4 <= len(value) <= 70):
        raise ValidationError('La descripción debe tener entre 4 y 50 caracteres.')