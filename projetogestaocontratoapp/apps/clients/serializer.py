from .models import Client
from rest_framework import serializers
from .models import Client, ClientCommunication

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
class ClientCommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCommunication
        fields = '__all__'
