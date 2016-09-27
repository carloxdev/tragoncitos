# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings

# Librerias Propias
from .views import Index
from .views import Login
from .views import Dashboard

urlpatterns = [

    url(
        r'^$',
        Index.as_view(),
        name='home.index'
    ),
    url(
        r'^login/$',
        Login.as_view(),
        name='home.login'
    ),
    url(
        r'^dashboard/$',
        Dashboard.as_view(),
        name='home.dashboard'
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        {'next_page': settings.LOGIN_URL},
        name='home.logout'
    )
]
