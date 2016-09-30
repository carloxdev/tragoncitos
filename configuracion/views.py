# -*- coding: utf-8 -*-

# Librerias Django:
from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Librerias Python:
from datetime import date

# Modelos
from .models import Alimento
from .models import Menu

# Formularios:
from .forms import AlimentoForm
from .forms import MenuForm

# Api Rest:
from rest_framework import viewsets

# Serializadores:
from .serializers import MenuSerializer


# ----------------- ALIMENTOS ----------------- #


@method_decorator(login_required, name='dispatch')
class AlimentoListView(generic.ListView):

    template_name = 'alimentos/alimento_lista.html'
    model = Alimento
    context_object_name = 'alimentos'
    paginate_by = 5


@method_decorator(login_required, name='dispatch')
class AlimentoCreateView(generic.CreateView):

    template_name = 'alimentos/alimento_nuevo.html'

    model = Alimento
    form_class = AlimentoForm

    def get_success_url(self):
        # return redirect(reverse('config.alimento_lista'), safe=False)
        return '/alimentos/'


@method_decorator(login_required, name='dispatch')
class AlimentoUpdateView(generic.UpdateView):

    template_name = 'alimentos/alimento_editar.html'

    model = Alimento
    form_class = AlimentoForm

    def get_success_url(self):
        # return redirect(reverse('config.alimento_lista'), safe=False)
        return '/alimentos/'


class AlimentoConsultar(generic.View):

    def __init__(self):
        self.template_name = 'alimentos/alimento_info.html'

    def get(self, request, pk):

        alimento = Alimento.objects.get(pk=pk)

        contexto = {
            'alimento': alimento
        }

        return render(request, self.template_name, contexto)


# ----------------- MENUS ----------------- #

@method_decorator(login_required, name='dispatch')
class MenuListView(generic.View):

    def __init__(self):
        self.template_name = 'menus/menu_lista.html'

    def get(self, request):
        return render(request, self.template_name, {})


@method_decorator(login_required, name='dispatch')
class MenuCreateView(generic.View):

    def __init__(self):
        self.template_name = 'menus/menu_nuevo.html'

    def get(self, request, year, month, day):

        fecha = date(int(year), int(month), int(day))

        formulario = MenuForm()

        contexto = {
            'fecha': fecha,
            'form': formulario
        }

        return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
class MenuUpdateView(generic.UpdateView):

    template_name = 'menus/menu_editar.html'

    model = Menu
    form_class = MenuForm

    def get_success_url(self):
        # return redirect(reverse('config.menu_lista'))
        return reverse_lazy('config.menu_lista')

# ----------------- APIS ----------------- #


class MenuAPI(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
