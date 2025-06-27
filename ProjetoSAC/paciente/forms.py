from django import forms
from paciente.models import Paciente

class PacienteForm(forms.ModelForm):
  class Meta:
    model = Paciente
    fields = ['nome', 'email', 'telefone', 'data_nascimento', 'sexo', 'cpf', 'foto']

  foto = forms.ImageField(
      label='Foto do paciente',
      widget=forms.FileInput(attrs={'class': 'form-control-file'}),
  )

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
        
    for field in ['nome', 'email', 'telefone', 'data_nascimento', 'sexo', 'cpf', 'foto']:
      self.fields[field].widget.attrs.update({'class': 'form-control'})
