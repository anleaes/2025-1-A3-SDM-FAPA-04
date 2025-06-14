from django.db import models

# Create your models here.
class Media(models.Model):
    name = models.CharField('Nome', max_length=150)
    description = models.TextField('Descricao', max_length=200)
    
    class Meta:
        verbose_name = 'Canal de Comunicação do Cliente'
        verbose_name_plural = 'Canais de Comunicação do Cliente'
        ordering =['id']

    def __str__(self):
        return self.name
