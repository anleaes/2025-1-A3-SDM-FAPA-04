from django.db import models


class ContractType(models.Model):
    name = models.CharField('Nome', max_length=50)
    descriptions = models.TextField('Descrição', max_length=100)
    
    class Meta:
        verbose_name = 'Tipo de Contrato'
        verbose_name_plural = 'Tipos de Contratos'
        ordering =['id']

    def __str__(self):
        return self.name