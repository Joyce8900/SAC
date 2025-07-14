from django.db import models
from medico.models import Medico
from paciente.models import Paciente
from django.core.validators import MinValueValidator
from django.utils import timezone

class Consulta(models.Model):
    STATUS_CHOICES = [
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
        ('falta', 'Falta'),
    ]
    
    TIPO_CHOICES = [
        ('consulta', 'Consulta'),
        ('retorno', 'Retorno'),
        ('exame', 'Exame'),
        ('cirurgia', 'Cirurgia'),
    ]
    
    paciente = models.ForeignKey(
        Paciente, 
        on_delete=models.CASCADE,
        related_name='consultas'
    )
    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        related_name='consultas'
    )
    data = models.DateTimeField(
        validators=[MinValueValidator(
            limit_value=timezone.now,
            message="Data não pode ser no passado"
        )]
    )
    tipo = models.CharField(
        max_length=20, 
        choices=TIPO_CHOICES,
        default='consulta'
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES,
        default='agendada'
    )
    observacoes = models.TextField(
        blank=True,
        null=True
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['data']
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        constraints = [
            models.UniqueConstraint(
                fields=['medico', 'data'],
                name='unique_consulta_medico_data'
            )
        ]

    def __str__(self):
        return f"{self.paciente.nome} com {self.medico.nome} - {self.get_status_display()}"

    @property
    def is_futura(self):
        return self.data > timezone.now()
