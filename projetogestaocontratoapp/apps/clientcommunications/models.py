from django.db import models

class ClientCommunication(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    communicationchannels = models.ForeignKey ('communicationchannels.CommunicationChannel', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Canal de Comunicação com o Cliente'
        verbose_name_plural = 'Canais de comunicação com o cliente'
        ordering =['id']

    def __str__(self):
        return self.client
