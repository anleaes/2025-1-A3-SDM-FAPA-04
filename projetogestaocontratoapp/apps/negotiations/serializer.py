from .models import Negotiation
from bodycontracts.models import BodyContract 
from rest_framework import serializers

class NegotiationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negotiation
        fields = '__all__'

