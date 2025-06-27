from django import forms
from paciente.models import Paciente

class PacienteForm(forms.ModelForm):
  data_nascimento = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],  # Formatos aceitos
        widget=forms.DateInput(attrs={'type': 'date'})  # Opcional: usa o widget de data nativo do HTML5
    )

  SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
  sexo = forms.CharField(label='Sexo', widget=forms.Select(choices=SEXO_CHOICES))

  foto = forms.ImageField(
      label='Foto do paciente',
      widget=forms.FileInput(attrs={'class': 'form-control-file'}),
  )

  class Meta:
    model = Paciente
    fields = ['nome', 'email', 'telefone', 'data_nascimento', 'sexo', 'cpf', 'foto']

  

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
        
    for field in ['nome', 'email', 'telefone', 'data_nascimento', 'sexo', 'cpf', 'foto']:
      self.fields[field].widget.attrs.update({'class': 'form-control'})
