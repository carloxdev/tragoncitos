# -*- coding: utf-8 -*-

# Django API REST
from rest_framework import filters
import django_filters

# Modelos
from .models import Menu


def filter_ByMes(queryset, value):

    if not value:
        return queryset
    else:
        consulta = queryset.filter(dia__month=value)
        return consulta


def filter_ByYear(queryset, value):

    if not value:
        return queryset
    else:
        consulta = queryset.filter(dia__year=value)
        return consulta


class MenuFilter(filters.FilterSet):

    anio = django_filters.CharFilter(action=filter_ByYear)
    mes = django_filters.CharFilter(action=filter_ByMes)

    class Meta:
        model = Menu
        fields = [
            'anio',
            'mes',
        ]
