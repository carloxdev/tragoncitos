# -*- coding: utf-8 -*-

# Librerias Django
from django.forms import ModelForm
from django.forms import Textarea
from django.forms import TextInput
from django.forms import Select

# Modelos:
from .models import Alimento
from .models import Menu


class AlimentoForm(ModelForm):

    class Meta:
        model = Alimento
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'descripcion': Textarea(attrs={'class': 'form-control'}),
            'tipo': Select(attrs={'class': 'form-control'}),
            'restaurante': Select(attrs={'class': 'form-control'}),
        }


class MenuForm(ModelForm):

    class Meta:
        model = Menu
        fields = '__all__'
