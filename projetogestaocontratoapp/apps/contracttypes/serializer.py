from django.shortcuts import render
from .models import ContractType
from rest_framework import serializers

class ContractTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractType
        fields = '__all__'
     