# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import ReservacionNueva
from .views import ReservacionGracias
from .views import ReservacionLista

urlpatterns = [

    url(
        r'^reservaciones/$',
        ReservacionLista.as_view(),
        name='reserva.lista'
    ),
    url(
        r'^reservacion/nueva/(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$',
        ReservacionNueva.as_view(),
        name='reserva.nueva'
    ),
    url(r'^reservaciones/gracias/(?P<pk>.*)/$',
        ReservacionGracias.as_view(),
        name='reserva.gracias'
        ),
]
