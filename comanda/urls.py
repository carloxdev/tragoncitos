# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import ReservacionNueva
from .views import ReservacionGracias
from .views import ReservacionLista

urlpatterns = [

    url(
        r'^comanda/reservaciones/$',
        ReservacionLista.as_view(),
        name='comanda.reserva_lista'
    ),
    url(
        r'^comanda/reservaciones/nueva/(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$',
        ReservacionNueva.as_view(),
        name='comanda.reserva_nueva'
    ),
    url(r'^comanda/reservaciones/gracias/(?P<pk>.*)/$',
        ReservacionGracias.as_view(),
        name='comanda.reserva_gracias'
        ),
]
