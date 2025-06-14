from django.shortcuts import render
from .models import Negotiation, ContractVersion  
from rest_framework import viewsets
from .serializer import NegotiationSerializer, ContractVersionSerializer

# Create your views here.
class NegotiationViewSet(viewsets.ModelViewSet):
    queryset = Negotiation.objects.all()
    serializer_class = NegotiationSerializer 
     
class ContractVersionViewSet(viewsets.ModelViewSet):
    queryset = ContractVersion.objects.all()
    serializer_class = ContractVersionSerializer 
