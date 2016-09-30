# -*- coding: utf-8 -*-

# Modelos
from .models import Menu

# Librerias de terceros:
from rest_framework import serializers


class MenuSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Menu
        fields = (
            'dia',
            'descripcion',
        )
