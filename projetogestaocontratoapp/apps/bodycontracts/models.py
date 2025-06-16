from django.db import models
from negotiations.models import Negotiation
from contracts import Contract


class BodyContract (models.Model):        
    negotiation = models.ForeignKey(Negotiation, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE,related_name='versions', verbose_name='Contrato')
    clause = models.TextField('Clausula', blank=True, null=True)
    title_clause = models.CharField('Titulo da Clausula', max_length=100)
    quantity_clause = models.IntegerField('Numero de clausula',null=True, blank=True,default=0)
    
    class Meta:
        unique_together = ('negotiation', 'contract')
        verbose_name = 'Corpo do contrato'
        verbose_name_plural = 'Corpo dos Contratos'
        ordering =['id']

    def __str__(self):
        return f"{self.quantity_clause} - {self.contract.name}"