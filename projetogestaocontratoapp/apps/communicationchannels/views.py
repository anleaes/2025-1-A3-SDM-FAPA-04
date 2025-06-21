from django.shortcuts import render
from .models import CommunicationChannel
from rest_framework import viewsets
from .serializer import CommunicationChannelSerializer

# Create your views here.
class CommunicationchannelViewSet(viewsets.ModelViewSet):
    queryset = CommunicationChannel.objects.all()
    serializer_class = CommunicationChannelSerializer  

