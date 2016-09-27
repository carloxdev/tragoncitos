# -*- coding: utf-8 -*-

# Librerias django
from django.contrib import admin


# Modelos:
from .models import Reservacion


@admin.register(Reservacion)
class AdminRestaurante(admin.ModelAdmin):
    list_display = (
        'dia',
        'persona',
        'empresa',
        'correo',
        'entrada',
        'plato_fuerte',
        'guarnicion',
        'ensalada',
        'postre',
        'agua',
        'comentarios',
    )
