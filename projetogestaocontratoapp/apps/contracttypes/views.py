from django.shortcuts import render
from .models import ContractType
from rest_framework import viewsets
from .serializer import ContractTypeSerializer


class ContractTypeViewSet(viewsets.ModelViewSet):
    queryset = ContractType.objects.all()
    serializer_class = ContractTypeSerializer  