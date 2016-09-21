# -*- coding: utf-8 -*-

# Librerias django
from django.contrib import admin


# Modelos:
from .models import Restaurante
from .models import Alimento
from .models import Menu


@admin.register(Restaurante)
class AdminRestaurante(admin.ModelAdmin):
    list_display = (
        'nombre',
        'logo',
        'activo',
        'correo',
    )


@admin.register(Alimento)
class AdminAlimento(admin.ModelAdmin):
    list_display = (
        'nombre',
        'descripcion',
        'foto',
        'tipo',
        'activo',
        'restaurante',
    )


@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    list_display = (
        'dia',
        'descripcion',
    )
    filter_horizontal = ('alimentos',)
