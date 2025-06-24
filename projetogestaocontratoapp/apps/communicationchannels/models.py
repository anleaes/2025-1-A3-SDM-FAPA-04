from django.db import models

# Create your models here.
class CommunicationChannel(models.Model):
    name = models.CharField('Nome', max_length=50)
    definition= models.TextField('Definição', max_length=100)
        
    class Meta:
        verbose_name = 'Canal de Comunicação'
        verbose_name_plural = 'Canais de Comunicação'
        ordering =['id']

    def __str__(self):
        return self.name