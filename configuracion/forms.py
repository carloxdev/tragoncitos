# -*- coding: utf-8 -*-

# Librerias Django
from django.forms import ModelForm
from django.forms import Textarea
from django.forms import TextInput
from django.forms import Select
from django.forms import SelectMultiple
from django.forms import CheckboxSelectMultiple
from django.forms.extras import SelectDateWidget
from django.forms import DateField
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelMultipleChoiceField


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

    # dia = DateField(widget=SelectDateWidget)
    # alimentos = ModelMultipleChoiceField(
    #     queryset=Alimento.objects.all(),
    #     widget=SelectMultiple
    # )

    class Meta:
        model = Menu
        fields = '__all__'
        exclude = ['dia']
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'alimentos': SelectMultiple(attrs={'class': 'form-control height-full'})
        }
