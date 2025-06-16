from .models import CommunicationChannel
from rest_framework import serializers

class CommunicationChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationChannel
        fields = '__all__'