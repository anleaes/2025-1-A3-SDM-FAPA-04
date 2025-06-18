from django.shortcuts import render
from .models import BodyContract
from rest_framework import viewsets
from .serializer import  BodyContractSerializer


    
class BodyContractViewSet(viewsets.ModelViewSet):
    queryset = BodyContract.objects.all()
    serializer_class = BodyContractSerializer  

