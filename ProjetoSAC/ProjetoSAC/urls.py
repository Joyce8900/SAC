from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("medicos/", include("medico.urls")),
    path("pacientes/", include("paciente.urls")),
    path("usuarios/", include("usuarios.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 