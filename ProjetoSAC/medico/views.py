from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Medico
from .forms import MedicoForm

# Create your views here.

class MedicoListView(ListView):
  model = Medico
  template_name = 'listar.html'
  context_object_name = 'medicos'

class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'cadastro.html'
    success_url = '/medicos/' # Redirect after successful creation
    def form_valid(self, form):
        return super().form_valid(form)