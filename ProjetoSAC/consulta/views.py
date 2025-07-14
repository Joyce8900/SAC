from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Consulta
from .forms import ConsultaForm
from medico.models import Medico
from paciente.models import Paciente
from django.utils import timezone

class AgendarConsultaView(LoginRequiredMixin, View):
    template_name = 'consulta/agendar.html'
    
    def get(self, request):
        form = ConsultaForm()
        medicos = Medico.objects.all()
        pacientes = Paciente.objects.all()
        return render(request, self.template_name, {
            'form': form,
            'medicos': medicos,
            'pacientes': pacientes
        })
    
    def post(self, request):
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.criado_por = request.user
            consulta.save()
            messages.success(request, 'Consulta agendada com sucesso!')
            return redirect('consulta:lista')
        return render(request, self.template_name, {'form': form})

class ListaConsultasView(LoginRequiredMixin, View):
    template_name = 'consulta/lista.html'
    
    def get(self, request):
        hoje = timezone.now().date()
        consultas = Consulta.objects.filter(
            data__date__gte=hoje
        ).order_by('data')
        
        return render(request, self.template_name, {
            'consultas': consultas,
            'hoje': hoje
        })

class DetalheConsultaView(LoginRequiredMixin, View):
    template_name = 'consulta/detalhe.html'
    
    def get(self, request, pk):
        consulta = Consulta.objects.get(pk=pk)
        return render(request, self.template_name, {'consulta': consulta})