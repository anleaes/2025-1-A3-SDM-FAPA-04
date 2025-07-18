from django.db import models


class Negotiation(models.Model):
    total_value = models.FloatField('Valor Total', null=True, blank=True, default=0.0, help_text='Valor em Reais')
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Aprovado', 'Aprovado'),
        ('Pendente', 'Pendente'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    contract = models.ForeignKey ('contracts.Contract', on_delete=models.CASCADE)
       
    class Meta:
        verbose_name = 'negociação'
        verbose_name_plural = 'negociações'
        ordering =['id']

    def __str__(self):
        return f"{self.status} - {self.client}"