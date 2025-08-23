from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data', 'tipo', 'status')
    list_filter = ('status', 'tipo', 'medico__especialidade')
    search_fields = ('paciente__nome', 'medico__nome')
    date_hierarchy = 'data'
    ordering = ('-data',)