from django.shortcuts import render
from .models import Contract
from rest_framework import viewsets
from .serializer import ContractSerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer  


