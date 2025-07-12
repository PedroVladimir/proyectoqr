from django.core.validators import ValidationError

def validate_texto_length(value):
    if ( 4 <= len(value) <= 20):
        raise ValidationError('El texto debe tener entre 4 y 20 caracteres.')

def validate_descripcion_length(value):
    if ( 4 <= len(value) <= 50):
        raise ValidationError('La descripción debe tener entre 4 y 50 caracteres.')
    


