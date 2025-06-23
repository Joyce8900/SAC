from django.urls import path
from medico.views import MedicoListView, MedicoCreateView  # Importe diretamente da app

urlpatterns = [
    path('', MedicoListView.as_view(), name='medicos'),
    path('cadastro/', MedicoCreateView.as_view(), name='cadastro'),
]