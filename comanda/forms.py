# -*- coding: utf-8 -*-

# Librerias Django
from django.forms import ModelForm
from django.forms import HiddenInput
from django.forms import Textarea
from django.forms import TextInput
from django.forms import Select

# Modelos:
from .models import Reservacion

# Otros Modelos:
from configuracion.models import Menu


class ReservacionForm(ModelForm):

    class Meta:
        model = Reservacion
        fields = '__all__'
        widgets = {
            'persona': TextInput(attrs={'class': 'form-control'}),
            'comentarios': Textarea(attrs={'class': 'form-control'}),
            'correo': TextInput(attrs={'class': 'form-control'}),
            'empresa': TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, _date, *args, **kwargs):
        super(ReservacionForm, self).__init__(*args, **kwargs)

        self.fields['dia'].widget = HiddenInput()
        self.fields['dia'].initial = _date

        menu = Menu.objects.get(dia=_date)

        # import ipdb; ipdb.set_trace()

        self.fields['entrada'].widget = Select(
            attrs={'class': 'form-control'}
        )
        self.fields['entrada'].queryset = menu.alimentos.filter(tipo='ENT')

        self.fields['plato_fuerte'].widget = Select(
            attrs={'class': 'form-control'}
        )
        self.fields["plato_fuerte"].queryset = menu.alimentos.filter(
            tipo='FUE'
        )

        self.fields['ensalada'].widget = Select(
            attrs={'class': 'form-control'}
        )
        self.fields["ensalada"].queryset = menu.alimentos.filter(
            tipo='ENS'
        )

        self.fields['postre'].widget = Select(
            attrs={'class': 'form-control'})
        self.fields["postre"].queryset = menu.alimentos.filter(
            tipo='POS'
        )

        self.fields['agua'].widget = Select(
            attrs={'class': 'form-control'}
        )
        self.fields["agua"].queryset = menu.alimentos.filter(
            tipo='AGU'
        )
