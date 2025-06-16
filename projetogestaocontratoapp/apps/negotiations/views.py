from django.shortcuts import render
from .models import Negotiation
from rest_framework import viewsets
from .serializer import NegotiationSerializer

# Create your views here.
class NegotiationViewSet(viewsets.ModelViewSet):
    queryset = Negotiation.objects.all()
    serializer_class = NegotiationSerializer 
     
