from django.db import models
from Media.models import Media
# Create your models here.

class Client(models.Model):
    name = models.CharField('Nome', max_length=150)
    social_security_number = models.CharField('CPF', max_length=11)
    occupation = models.CharField('Profissão', max_length=200)   
    MARITAL_STATUS_CHOICES = (
    ('S', 'Solteiro(a)'),
    ('C', 'Casado(a)'),
    ('D', 'Divorciado(a)'),
    ('V', 'Viúvo(a)'),
    ('U', 'União Estável'),
)
    marital_status = models.CharField('Estado Civil', max_length=1, choices=MARITAL_STATUS_CHOICES)
    client_communication = models.ManyToManyField(Media, through='ClientCommunication', blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.name
