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
        r'^alimentos/$',
        AlimentoListView.as_view(),
        name='config.alimento_lista'
    ),
    url(
        r'^alimentos/nuevo/$',
        AlimentoCreateView.as_view(),
        name='config.alimento_nuevo'
    ),
    url(
        r'^alimentos/editar/(?P<pk>[0-9]+)/$',
        AlimentoUpdateView.as_view(),
        name='config.alimento_editar'
    ),
    url(
        r'^alimento/consultar/(?P<pk>[0-9])/$',
        AlimentoConsultar.as_view(),
        name='config.alimento_consultar'
    ),


    # ----------------- MENUS ----------------- #

    url(
        r'^menus/$',
        MenuListView.as_view(),
        name='config.menu_lista'
    ),

    url(
        r'^menus/nuevo/$',
        MenuCreateView.as_view(),
        name='config.menu_nuevo'
    ),

    url(
        r'^menus/editar/(?P<pk>[0-9]+)/$',
        MenuUpdateView.as_view(),
        name='config.menu_editar'
    ),
]
