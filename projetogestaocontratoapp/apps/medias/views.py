from django.shortcuts import render
from .models import Media
from rest_framework import viewsets
from .serializer import MediaSerializer

# Create your views here.
class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer  
