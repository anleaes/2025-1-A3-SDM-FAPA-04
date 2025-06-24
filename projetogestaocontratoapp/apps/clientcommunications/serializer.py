from .models import ClientCommunication
from rest_framework import serializers

class ClientCommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCommunication
        fields = '__all__'
