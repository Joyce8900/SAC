from django.urls import path
from paciente.views import PacienteListView, PacienteCreateView

urlpatterns = [
  path('', PacienteListView.as_view(), name='pacientes:pacientes'),
  path('cadastro/', PacienteCreateView.as_view(), name='cadastro'),
 
]