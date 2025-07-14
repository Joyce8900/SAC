from datetime import timezone
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Medico
from .forms import MedicoForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


URL = '/medicos/'
# Create your views here.

@method_decorator(login_required, name='dispatch')
class MedicoListView(ListView):
  model = Medico
  template_name = 'medico/medico_listar.html'
  context_object_name = 'medicos'

class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/medico_cadastro.html'
    success_url = URL 
    

class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/medico_editar.html'
    success_url = URL
    slug_field = 'crm'
    slug_url_kwarg = 'crm'

class MedicoDetailView(DetailView):
    model = Medico
    template_name = 'medico/medico_detalhe.html'
    context_object_name = URL
    slug_field = 'crm'
    slug_url_kwarg = 'crm'

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'medico/medico_excluir.html'
    slug_field = 'crm'
    slug_url_kwarg = 'crm'
    success_url = URL
    