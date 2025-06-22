from django.shortcuts import render
from .models import ClientCommunication
from rest_framework import viewsets
from .serializer import ClientCommunicationSerializer

class ClientCommunicationViewSet(viewsets.ModelViewSet):
  queryset = ClientCommunication.objects.all()
  serializer_class = ClientCommunicationSerializer