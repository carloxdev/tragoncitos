# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import AlimentoListView
from .views import AlimentoCreateView
from .views import AlimentoUpdateView
from .views import AlimentoConsultar

from .views import MenuListView
from .views import MenuCreateView
from .views import MenuUpdateView


urlpatterns = [

    # ----------------- ALIMENTOS ----------------- #

    url(
        r'^configuracion/alimentos/$',
        AlimentoListView.as_view(),
        name='config.alimento_lista'
    ),
    url(
        r'^configuracion/alimentos/nuevo/$',
        AlimentoCreateView.as_view(),
        name='config.alimento_nuevo'
    ),
    url(
        r'^configuracion/alimentos/editar/(?P<pk>[0-9]+)/$',
        AlimentoUpdateView.as_view(),
        name='config.alimento_editar'
    ),
    url(
        r'^configuracion/alimentos/consultar/(?P<pk>[0-9])/$',
        AlimentoConsultar.as_view(),
        name='config.alimento_consultar'
    ),


    # ----------------- MENUS ----------------- #

    url(
        r'^configuracion/menus/$',
        MenuListView.as_view(),
        name='config.menu_lista'
    ),

    url(
        r'^configuracion/menus/nuevo/(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$',
        MenuCreateView.as_view(),
        name='config.menu_nuevo'
    ),

    url(
        r'^configuracion/menus/editar/(?P<pk>[0-9]+)/$',
        MenuUpdateView.as_view(),
        name='config.menu_editar'
    ),

]
