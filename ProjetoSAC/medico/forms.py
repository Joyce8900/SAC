from django import forms
from .models import Medico

class MedicoForm(forms.ModelForm):
    foto = forms.ImageField(
        label='Foto do médico',
        widget=forms.FileInput(attrs={'class': 'form-control-file'}),
    )

    class Meta:
        model = Medico
        fields = ['crm', 'nome', 'especialidade', 'foto']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicando classe 'form-control' aos outros campos (exceto o avatar que já tem)
        for field in ['crm', 'nome', 'especialidade', 'foto']:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
