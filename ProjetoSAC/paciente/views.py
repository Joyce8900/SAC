from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Paciente
from .forms import PacienteForm

URL = '/pacientes/'


class PacienteListView(ListView):
  model = Paciente
  template_name =  'paciente/paciente_listar.html'
  context_object_name = 'pacientes'

class PacienteDetailView(DetailView):
  model = Paciente
  template_name = 'paciente/paciente_detalhe.html'
  context_object_name = 'paciente'
  slug_field = 'cpf'
  slug_url_kwarg = 'cpf'
  
class PacienteDeleteView(DeleteView):
  model = Paciente
  template_name = 'paciente/paciente_excluir.html'
  slug_field = 'cpf'
  slug_url_kwarg = 'cpf'
  success_url = URL

class PacienteUpdateView(UpdateView):
  model = Paciente
  form_class = PacienteForm
  template_name = 'paciente/paciente_editar.html'
  success_url = URL
  slug_field = 'cpf'
  slug_url_kwarg = 'cpf'


class PacienteCreateView(CreateView):
  model = Paciente
  form_class = PacienteForm
  template_name = 'paciente/paciente_cadastro.html'
  success_url = URL