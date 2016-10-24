# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

#  API Rest
from rest_framework import routers

# Views
from configuracion.views import MenuAPI

router = routers.DefaultRouter()
router.register(r'menus', MenuAPI)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('configuracion.urls')),
    url(r'^', include('comanda.urls')),
    url(r'^', include('home.urls')),

    # API REST
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]


if settings.DEBUG:

    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
