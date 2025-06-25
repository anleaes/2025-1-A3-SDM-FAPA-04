from django.db import models

class ClientCommunication(models.Model):
   # client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    communicationchannels = models.ManyToManyField ('communicationchannels.CommunicationChannel', verbose_name='canal de comunicação')
    contact_value = models.CharField('Contato', max_length=255)
    
    class Meta:
        verbose_name = 'Canal de Comunicação com o Cliente'
        verbose_name_plural = 'Canais de comunicação com o cliente'
        ordering =['id']

    def __str__(self):
       return self.contact_value
  