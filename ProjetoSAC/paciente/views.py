from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Paciente
from .forms import PacienteForm

URL = '/pacientes/'

# Create your views here.
class PacienteListView(ListView):
  model = Paciente
  template_name =  'paciente_listar.html'
  context_object_name = 'pacientes'

# class PacienteDetailView(ListView):
#   model = Paciente
#   template_name = 'detalhe.html'
#   context_object_name = 'paciente'
#   slug_field = 'cpf'
#   slug_url_kwarg = 'cpf'
  
# class PacienteDeleteView(ListView):
#   model = Paciente
#   template_name = 'excluir.html'
#   slug_field = 'cpf'
#   slug_url_kwarg = 'cpf'
#   success_url = URL

# class PacienteUpdateView(ListView):
#   model = Paciente
#   form_class = PacienteForm
#   template_name = 'editar.html'
#   success_url = URL
#   slug_field = 'cpf'
#   slug_url_kwarg = 'cpf'


class PacienteCreateView(CreateView):
  model = Paciente
  form_class = PacienteForm
  template_name = 'paciente_cadastro.html'
  success_url = URL