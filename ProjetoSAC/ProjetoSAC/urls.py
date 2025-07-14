from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('medicos/', include('medico.urls')),  # Alterado de 'medicos' para 'medico'
    path('pacientes/', include('paciente.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('consulta/', include('consulta.urls', namespace='consulta')),
]