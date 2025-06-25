from django.urls import path
from medico.views import MedicoListView, MedicoCreateView, MedicoUpdateView, MedicoDetailView, MedicoDeleteView 

urlpatterns = [
    path('', MedicoListView.as_view(), name='medicos'),
    path('cadastro/', MedicoCreateView.as_view(), name='cadastro'),
    path('editar/<str:crm>/', MedicoUpdateView.as_view(), name='editar'),
    path('detalhe/<str:crm>/', MedicoDetailView.as_view(), name='detalhe'),
    path('excluir/<int:pk>/', MedicoDeleteView.as_view(), name='excluir'),
]