# -*- coding: utf-8 -*-

# Librerias Django
from __future__ import unicode_literals
from django.db import models


ALIMENTO_TIPO = (
    ('ENT', 'ENTRADA'),
    ('FUE', 'PLATO FUERTE'),
    ('GUA', 'GUARNICION'),
    ('ENS', 'ENSALADA'),
    ('POS', 'POSTRE'),
    ('AGU', 'AGUA'),
)


class Restaurante(models.Model):
    nombre = models.CharField(max_length=140)
    logo = models.ImageField(upload_to='media/restaurantes', blank=True, null=True)
    activo = models.BooleanField(default=True)
    correo = models.EmailField(max_length=254)

    def __str__(self):
        return self.nombre


class Alimento(models.Model):
    nombre = models.CharField(max_length=140)
    descripcion = models.TextField(blank=True)
    foto = models.ImageField(upload_to='alimentos', blank=True)
    tipo = models.CharField(max_length=3, choices=ALIMENTO_TIPO)
    activo = models.BooleanField(default=True)
    restaurante = models.ForeignKey(Restaurante)

    def __str__(self):
        return self.nombre


class Menu(models.Model):
    dia = models.DateField(unique=True)
    descripcion = models.CharField(max_length=140, blank=True)
    alimentos = models.ManyToManyField(Alimento)

    def __str__(self):
        return "{} - {}".format(self.dia, self.descripcion)
