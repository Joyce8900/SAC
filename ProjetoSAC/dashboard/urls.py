from django.urls import path
from .views import DashboardView  # Importe a classe que você criou

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),  # Use as_view() para class-based views
]