from django.db import models

class Medico(models.Model):
  crm = models.CharField(max_length=6, unique=True, verbose_name='CRM', primary_key=True, blank=False, null=False)
  nome = models.CharField(max_length=100, blank=False, null=False)
  especialidade = models.CharField(max_length=100, blank=False, null=False)
  foto = models.ImageField(
        upload_to='medicos_fotos/',  
        blank=True, 
        null=True,
        verbose_name='Foto do Médico'
    )

  def __str__(self):
    return self.nome
  
class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
    
