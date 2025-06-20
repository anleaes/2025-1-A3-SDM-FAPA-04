from django.db import models



# Create your models here.
class Negotiation(models.Model):
    total_value = models.FloatField('Valor Total', null=True, blank=True, default=0.0)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Aprovado', 'Aprovado'),
        ('Pendente', 'Pendente'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    body_contract = models.ManyToManyField('contracts.Contract', blank=True)
    
    class Meta:
        verbose_name = 'Negociação'
        verbose_name_plural = 'Negociações'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.client) 
    