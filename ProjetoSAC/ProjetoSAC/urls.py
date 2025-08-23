from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('medicos/', include('medico.urls')),  # Alterado de 'medicos' para 'medico'
    path('pacientes/', include('paciente.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('consulta/', include('consulta.urls', namespace='consulta')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)