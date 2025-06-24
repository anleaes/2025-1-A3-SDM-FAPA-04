from django.db import models

class BodyContract(models.Model):        
    negotiation = models.ForeignKey('negotiations.Negotiation', on_delete=models.CASCADE)
    contract_father = models.ForeignKey('contracts.Contract', on_delete=models.CASCADE)
    clause = models.TextField('Clausula', blank=True, null=True)
    title_clause = models.CharField('Titulo da Clausula', max_length=100)
    quantity_clause = models.IntegerField('Numero da clausula', null=True, blank=True,default=0)
    


    class Meta:
        #unique_together = ('contract_father')
        verbose_name = 'Corpo do contrato'
        verbose_name_plural = 'Itens do contrato'
        ordering =['id']

    def __str__(self):
        return self.contract_father
    


    # class Meta:
    #     verbose_name = 'Corpo do contrato'
    #     verbose_name_plural = 'Corpo dos Contratos'
    #     ordering =['id']

    # def __str__(self):
    #     return self.negotiation


    