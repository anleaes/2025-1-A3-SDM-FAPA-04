from django.db import models


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
    communicationchannel = models.ManyToManyField('communicationchannels.CommunicationChannel', blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.name
    
class ClientCommunication(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    communication_channel = models.ForeignKey('communicationchannels.CommunicationChannel', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Canal de Comunicação com o Cliente'
        verbose_name_plural = 'Canais de Comunicação com o Cliente'
        ordering =['id']

    def __str__(self):
        return self.communication_channel.name 
    
