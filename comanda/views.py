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
        self.template_name = 'recervaciones/reservar_nueva.html'

    def get(self, request, year, month, day):

        fecha = date(int(year), int(month), int(day))

        entradas = []
        platos_fuertes = []
        guarniciones = []
        ensaladas = []
        postres = []
        aguas = []

        mensaje = ''

        try:
            menu = Menu.objects.get(dia=fecha)

            alimentos = menu.alimentos.all()

            for alimento in alimentos:
                if alimento.tipo == 'ENT':
                    entradas.append(alimento)

                elif alimento.tipo == 'FUE':
                    platos_fuertes.append(alimento)

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
            'dia': fecha,
            'entradas': entradas,
            'platos_fuertes': platos_fuertes,
            'guarniciones': guarniciones,
            'ensaladas': ensaladas,
            'postres': postres,
            'aguas': aguas,
            'mensaje': mensaje
        }

        return render(request, self.template_name, contexto)

    def post(self, request, year, month, day):

        entradas = []
        platos_fuertes = []
        guarniciones = []
        ensaladas = []
        postres = []
        aguas = []

        mensaje = ''
        error = ''

        fecha = date(int(year), int(month), int(day))

        persona = request.POST.get('id_persona')
        empresa = request.POST.get('id_empresa')
        correo = request.POST.get('id_correo')
        comentarios = request.POST.get('id_comentarios')

        entrada_pk = request.POST.get('entrada')
        plato_fuete_pk = request.POST.get('plato_fuete')
        guarnicion_pk = request.POST.get('guarnicion')
        ensalada_pk = request.POST.get('ensalada')
        postre_pk = request.POST.get('postre')
        agua_pk = request.POST.get('agua')

        import ipdb; ipdb.set_trace() 

        # Validar datos
        if persona != '':
            try:

                reservacion = Reservacion()

                reservacion.dia = fecha

                if entrada_pk:
                    reservacion.entrada = Alimento.objects.get(
                        pk=entrada_pk.encode('utf-8'))

                if plato_fuete_pk:
                    reservacion.plato_fuerte = Alimento.objects.get(
                        pk=plato_fuete_pk.encode('utf-8')
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
                    'reserva.gracias',
                    kwargs={'pk': reservacion.id}
                ))

            except Exception, e:
                mensaje = str(e)
        else:
            try:
                menu = Menu.objects.get(dia=fecha)

                alimentos = menu.alimentos.all()

                for alimento in alimentos:
                    if alimento.tipo == 'ENT':
                        entradas.append(alimento)

                    elif alimento.tipo == 'FUE':
                        platos_fuertes.append(alimento)

                    elif alimento.tipo == 'GUA':
                        guarniciones.append(alimento)

                    elif alimento.tipo == 'ENS':
                        ensaladas.append(alimento)

                    elif alimento.tipo == 'POS':
                        postres.append(alimento)

                    elif alimento.tipo == 'AGU':
                        aguas.append(alimento)

                error = 'Favor de proporcionar el nombre de la persona que reserva'

            except Exception:
                mensaje = "No existe un Menú para este dia"

        contexto = {
            'dia': fecha,
            'entradas': entradas,
            'platos_fuertes': platos_fuertes,
            'guarniciones': guarniciones,
            'ensaladas': ensaladas,
            'postres': postres,
            'aguas': aguas,
            'error': error,
            'mensaje': mensaje
        }

        return render(request, self.template_name, contexto)


class ReservacionEditar(generic.View):

    def __init__(self):
        self.template_name = 'reservaciones/reservar_editar.html'


class ReservacionGracias(generic.View):

    def __init__(self):
        self.template_name = 'recervaciones/reservar_gracias.html'

    def get(self, request, pk):

        registro = Reservacion.objects.get(pk=pk)

        contexto = {
            'reservacion': registro
        }

        return render(request, self.template_name, contexto)


class ReservacionLista(generic.View):

    def __init__(self):
        self.template_name = 'recervaciones/reservar_lista.html'

    def get(self, request):

        fecha = date.today()
        reservaciones = Reservacion.objects.filter(dia=fecha)

        contexto = {
            'dia': fecha,
            'reservaciones': reservaciones
        }

        return render(request, self.template_name, contexto)
