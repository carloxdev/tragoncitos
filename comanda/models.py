# -*- coding: utf-8 -*-

# Librerias Django
from __future__ import unicode_literals
from django.db import models

# Otros Modelos:
from configuracion.models import Alimento


class Reservacion(models.Model):

    dia = models.DateField()
    persona = models.CharField(max_length=255)
    entrada = models.ForeignKey(
        Alimento,
        related_name='menu_entrada',
        blank=True,
        null=True
    )
    guarnicion = models.ForeignKey(
        Alimento,
        related_name='menu_guarnicion',
        blank=True,
        null=True
    )
    plato_fuerte = models.ForeignKey(
        Alimento,
        related_name='menu_plato_fuerte',
        blank=True,
        null=True
    )
    ensalada = models.ForeignKey(
        Alimento,
        related_name='menu_ensalada',
        blank=True,
        null=True
    )
    postre = models.ForeignKey(
        Alimento,
        related_name='menu_postre',
        blank=True,
        null=True)
    agua = models.ForeignKey(
        Alimento,
        related_name='menu_agua',
        blank=True,
        null=True
    )
    comentarios = models.TextField(blank=True)
    correo = models.EmailField(max_length=254)
    empresa = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "{} : {}".format(self.persona, self.empresa)

    class Meta:
        verbose_name_plural = 'Reservaciones'
