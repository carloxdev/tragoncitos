# -*- coding: utf-8 -*-

# Librerias Django:
from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

# Librerias Python:
from datetime import date
# from datetime import datetime

# Modelos:
from .models import Reservacion

# Otros Modelos:
from configuracion.models import Menu
from configuracion.models import Alimento

# Formulario:
# from .forms import ReservacionForm


class ReservacionNueva(generic.View):

    def __init__(self):
        self.template_name = 'reservaciones/reservar_nueva.html'

    def get_Menu(self, _fecha):

        entradas = []
        platos_fuertes = []
        platos_fuertes_opcional = []
        guarniciones = []
        ensaladas = []
        postres = []
        aguas = []

        mensaje = ''

        try:
            menu = Menu.objects.get(dia=_fecha)

            alimentos = menu.alimentos.all()

            for alimento in alimentos:
                if alimento.tipo == 'ENT':
                    entradas.append(alimento)

                elif alimento.tipo == 'FUE':
                    platos_fuertes.append(alimento)
                    platos_fuertes_opcional.append(alimento)

                elif alimento.tipo == 'GUA':
                    guarniciones.append(alimento)

                elif alimento.tipo == 'ENS':
                    ensaladas.append(alimento)

                elif alimento.tipo == 'POS':
                    postres.append(alimento)

                elif alimento.tipo == 'AGU':
                    aguas.append(alimento)

        except Exception:
            mensaje = "No existe un Menú para este dia"

        contexto = {
            'fecha': _fecha,
            'entradas': entradas,
            'platos_fuertes': platos_fuertes,
            'platos_fuertes_opcional': platos_fuertes_opcional,
            'guarniciones': guarniciones,
            'ensaladas': ensaladas,
            'postres': postres,
            'aguas': aguas,
            'mensaje': mensaje,
        }

        return contexto

    def get(self, request, year, month, day):

        fecha = date(int(year), int(month), int(day))

        contexto = self.get_Menu(fecha)

        return render(request, self.template_name, contexto)

    def post(self, request, year, month, day):

        fecha = date(int(year), int(month), int(day))
        error = ''

        persona = request.POST.get('id_persona')
        empresa = request.POST.get('id_empresa')
        correo = request.POST.get('id_correo')
        comentarios = request.POST.get('id_comentarios')

        entrada_pk = request.POST.get('entrada')
        plato_fuerte_pk = request.POST.get('plato_fuete')
        plato_fuerte_opcional_pk = request.POST.get('plato_fuerte_opcional')
        guarnicion_pk = request.POST.get('guarnicion')
        ensalada_pk = request.POST.get('ensalada')
        postre_pk = request.POST.get('postre')
        agua_pk = request.POST.get('agua')

        # Validar datos
        if persona != '':
            try:

                reservacion = Reservacion()

                reservacion.dia = fecha

                if entrada_pk:
                    reservacion.entrada = Alimento.objects.get(
                        pk=entrada_pk.encode('utf-8'))

                if plato_fuerte_pk:
                    reservacion.plato_fuerte = Alimento.objects.get(
                        pk=plato_fuerte_pk.encode('utf-8')
                    )

                if plato_fuerte_opcional_pk:
                    reservacion.plato_fuerte_opcional = Alimento.objects.get(
                        pk=plato_fuerte_opcional_pk.encode('utf-8')
                    )

                if guarnicion_pk:
                    reservacion.guarnicion = Alimento.objects.get(
                        pk=guarnicion_pk.encode('utf-8')
                    )

                if ensalada_pk:
                    reservacion.ensalada = Alimento.objects.get(
                        pk=ensalada_pk.encode('utf-8')
                    )

                if postre_pk:
                    reservacion.postre = Alimento.objects.get(
                        pk=postre_pk.encode('utf-8')
                    )

                if agua_pk:
                    reservacion.agua = Alimento.objects.get(
                        pk=agua_pk.encode('utf-8')
                    )

                reservacion.persona = persona.encode('utf-8')

                if empresa != '':
                    reservacion.empresa = empresa.encode('utf-8')

                if correo != '':
                    reservacion.correo = correo.encode('utf-8')

                if comentarios != '':
                    reservacion.comentarios = comentarios.encode('utf-8')

                reservacion.save()

                return redirect(reverse(
                    'comanda.reserva_gracias',
                    kwargs={'pk': reservacion.pk}
                ))

            except Exception, e:
                error = str(e)
        else:
            error = 'Favor de proporcionar el nombre de la persona que reserva'

        contexto = self.get_Menu(fecha)

        contexto['error'] = error

        return render(request, self.template_name, contexto)


class ReservacionEditar(generic.View):

    def __init__(self):
        self.template_name = 'reservaciones/reservar_editar.html'


class ReservacionGracias(generic.View):

    def __init__(self):
        self.template_name = 'reservaciones/reservar_gracias.html'

    def get(self, request, pk):

        registro = Reservacion.objects.get(pk=pk)

        contexto = {
            'reservacion': registro
        }

        return render(request, self.template_name, contexto)


class ReservacionLista(generic.View):

    def __init__(self):
        self.template_name = 'reservaciones/reservar_lista.html'

    def get(self, request):

        fecha = date.today()
        reservaciones = Reservacion.objects.filter(dia=fecha)

        contexto = {
            'dia': fecha,
            'reservaciones': reservaciones
        }

        return render(request, self.template_name, contexto)
