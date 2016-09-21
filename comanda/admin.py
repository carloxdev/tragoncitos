# -*- coding: utf-8 -*-

# Librerias django
from django.contrib import admin


# Modelos:
from .models import Reservacion


@admin.register(Reservacion)
class AdminRestaurante(admin.ModelAdmin):
    list_display = (
        'entrada',
        'plato_fuerte',
        'guarnicion',
        'ensalada',
        'postre',
        'agua',
        'persona',
        'comentarios',
        'correo',
        'empresa',
    )
