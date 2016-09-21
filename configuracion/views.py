# -*- coding: utf-8 -*-

# Librerias Django:
from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Liberias Python
from datetime import date

# Modelos
from .models import Alimento
from .models import Menu

# Formularios:
from .forms import AlimentoForm
from .forms import MenuForm

# ----------------- ALIMENTOS ----------------- #


@method_decorator(login_required, name='dispatch')
class AlimentoListView(generic.ListView):

    template_name = 'alimentos/alimento_lista.html'
    model = Alimento
    context_object_name = 'alimentos'
    paginate_by = 4


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
class MenuListView(generic.ListView):

    template_name = 'menus/menu_lista.html'
    model = Menu
    context_object_name = 'menus'
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class MenuCreateView(generic.CreateView):

    template_name = 'menus/menu_nuevo.html'

    model = Menu
    form_class = MenuForm

    def get_success_url(self):
        return redirect(reverse('config.menu_lista'))


@method_decorator(login_required, name='dispatch')
class MenuUpdateView(generic.UpdateView):

    template_name = 'menus/menu_editar.html'

    model = Menu
    form_class = MenuForm

    def get_success_url(self):
        return redirect(reverse('config.menu_lista'))

