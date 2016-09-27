# -*- coding: utf-8 -*-

# Librerias django
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.base import View

# Librerias Python
from datetime import date

# Librerias Terceros

# Librerias Propias


class Index(View):

    def __init__(self):
        self.template_name = 'home/index.html'

    def get(self, request):

        return render(request, self.template_name, {})

    def post(self, request):

        fecha = date.today()

        print fecha.day
        print fecha.month
        print fecha.year

        return redirect(reverse(
            'comanda.reserva_nueva',
            kwargs={
                'year': fecha.year,
                'month': fecha.month,
                'day': fecha.day
            }
        ))


class Login(View):

    def __init__(self):
        self.template_name = 'home/login.html'

    def get(self, request):

        if request.user.is_authenticated():
            return redirect(reverse('home.dashboard'))

        else:
            return render(request, self.template_name, {})

    def post(self, request):

        mensaje = ''
        usuario = request.POST.get('user')
        contrasena = request.POST.get('password')

        user = authenticate(username=usuario, password=contrasena)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect(reverse('home.dashboard'))
            else:
                mensaje = "Cuenta desactivada"

        else:
            mensaje = "Cuenta usuario o contraseña no vaida"

        contexto = {
            'mensaje': mensaje
        }

        return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
class Dashboard(TemplateView):
    template_name = 'home/dashboard.html'
