from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        # Lista pública de módulos (a proteção real está nas views individuais)
        modules = [
            {'name': 'Médicos', 'url': 'medico:medicos'},
            {'name': 'Pacientes', 'url': 'paciente:pacientes'},
            {'name': 'Dashboard', 'url': 'dashboard'}
        ]
        
        return render(request, 'home/home.html', {'modules': modules})