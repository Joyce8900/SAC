from django.urls import path
from paciente.views import PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDetailView, PacienteDeleteView

app_name = 'paciente'

urlpatterns = [
  path('', PacienteListView.as_view(), name='pacientes'),
  path('cadastro/', PacienteCreateView.as_view(), name='cadastro'),
  path('editar/<int:pk>/', PacienteUpdateView.as_view(), name='editar'),
  path('detalhe/<int:pk>/', PacienteDetailView.as_view(), name='detalhe'),
  path('excluir/<int:pk>/', PacienteDeleteView.as_view(), name='excluir'),
 
]