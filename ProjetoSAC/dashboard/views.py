from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import timedelta
from medico.models import Medico
from paciente.models import Paciente
from consulta.models import Consulta
from django.db.models import Count
import json

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'stats': self.get_stats(),
            'chart_data': json.dumps(self.get_chart_data()),
            'proximas_consultas': self.get_proximas_consultas(),
            'consultas_hoje': self.get_consultas_hoje(),
            'medicos': Medico.objects.all()[:5],  # Adicione esta linha
            'current_date': timezone.now().strftime('%d/%m/%Y'),
        }
        return render(request, 'dashboard/dashboard.html', context)
    
    def get_stats(self):
        total_consultas = Consulta.objects.count()
        realizadas = Consulta.objects.filter(status='realizada').count()
        
        return {
            'total_medicos': Medico.objects.count(),
            'total_pacientes': Paciente.objects.count(),
            'consultas_hoje': Consulta.objects.filter(
                data__date=timezone.now().date()
            ).count(),
            'taxa_conclusao': round((realizadas / total_consultas * 100)) if total_consultas > 0 else 0,
        }
    
    def get_proximas_consultas(self):
        return Consulta.objects.filter(
            data__gte=timezone.now(),
            status='agendada'
        ).select_related('paciente', 'medico').order_by('data')[:5]
    
    def get_consultas_hoje(self):
        return Consulta.objects.filter(
            data__date=timezone.now().date()
        ).select_related('paciente', 'medico').order_by('data')
    
    def get_chart_data(self):
        return {
            'atendimentos_mensais': self.get_atendimentos_mensais(),
            'status_consultas': self.get_status_consultas(),
        }
    
    def get_atendimentos_mensais(self):
        meses = []
        dados = []
        hoje = timezone.now().date()
        
        for i in range(5, -1, -1):
            mes = hoje - timedelta(days=30*i)
            mes_str = mes.strftime('%b/%Y')
            meses.append(mes_str)
            
            inicio_mes = mes.replace(day=1)
            fim_mes = (mes.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
            
            count = Consulta.objects.filter(
                data__date__range=[inicio_mes, fim_mes],
                status='realizada'
            ).count()
            dados.append(count)
        
        return {
            'labels': meses,
            'data': dados,
            'color': '#4BC0C0'
        }
    
    def get_status_consultas(self):
        status = Consulta.objects.values('status').annotate(
            total=Count('id')
        )
        return {
            'labels': [s['status'].capitalize() for s in status],
            'data': [s['total'] for s in status],
            'colors': ['#36A2EB', '#4BC0C0', '#FFCE56', '#FF6384']
        }