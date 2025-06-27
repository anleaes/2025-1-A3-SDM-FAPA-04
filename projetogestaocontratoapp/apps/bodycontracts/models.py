from django.db import models

class BodyContract(models.Model):        
    clause = models.TextField('Clausula', blank=True, null=True)
    title_clause = models.CharField('Titulo da Clausula', max_length=100)
    quantity_clause = models.IntegerField('Numero de clausulas', null=True, blank=True,default=0)
    


    class Meta:
        verbose_name = 'Corpo do contrato'
        verbose_name_plural = 'Itens do contrato'
        ordering =['id']

    def __str__(self):
        return self.title_clause    