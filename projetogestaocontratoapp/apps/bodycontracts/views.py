from .models import BodyContract
from rest_framework import viewsets
from .serializer import  BodyContractSerializer

# Após o comentario "# Create your views here." e crie as views "Orderitem".
    
class OrderitemViewSet(viewsets.ModelViewSet):
    queryset = BodyContract.objects.all()
    serializer_class = BodyContractSerializer  

