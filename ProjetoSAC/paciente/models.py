import os
from django.db import models

# Create your models here.
class Paciente(models.Model):
  def foto(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{self.nome}.{ext}'
        return os.path.join('paciente_fotos/', filename)
  
  
  nome = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  telefone = models.CharField(max_length=20)
  data_nascimento = models.DateField()
  sexo = models.CharField(max_length=1)
  cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF', primary_key=True, blank=False, null=False)
  foto = models.ImageField(upload_to='pacientes_fotos/', blank=True, null=True, verbose_name='Foto do Paciente')

  
  

  def __str__(self):
    return self.nome