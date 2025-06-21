from django.shortcuts import render
from .models import Client
from rest_framework import viewsets
from .serializer import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
# from django.shortcuts import render
# from .models import Client, ClientCommunication
# from rest_framework import viewsets
# from .serializer import ClientSerializer, ClientCommunicationSerializer

# class ClientCommunicationViewSet(viewsets.ModelViewSet):
#   queryset = ClientCommunication.objects.all()
#   serializer_class = ClientCommunicationSerializer
