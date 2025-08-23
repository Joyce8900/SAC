from django.urls import path
from .views import (
    AgendarConsultaView,
    ListaConsultasView,
    DetalheConsultaView
)

app_name = 'consulta'

urlpatterns = [
    path('agendar/', AgendarConsultaView.as_view(), name='agendar'),
    path('lista/', ListaConsultasView.as_view(), name='lista'),
    path('<int:pk>/', DetalheConsultaView.as_view(), name='detalhe'),
]