from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import CommunicationChannel
from rest_framework import viewsets
from .serializer import CommunicationChannelSerializer

# Create your views here.
class CommunicationchannelViewSet(viewsets.ModelViewSet):
    queryset = CommunicationChannel.objects.all()
    serializer_class = CommunicationChannelSerializer  

