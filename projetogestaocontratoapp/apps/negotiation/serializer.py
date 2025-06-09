from .models import Negotiation, ContractVersion
from rest_framework import serializers

class NegotiationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negotiation
        fields = '__all__'

class ContractVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractVersion
        fields = '__all__'