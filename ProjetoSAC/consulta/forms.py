from django import forms
from .models import Consulta
from django.utils import timezone

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'data', 'tipo', 'observacoes']
        widgets = {
            'data': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def clean_data(self):
        data = self.cleaned_data['data']
        if data < timezone.now():
            raise forms.ValidationError("Não é possível agendar consultas no passado")
        return data