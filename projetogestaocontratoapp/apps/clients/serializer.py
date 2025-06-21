from .models import Client
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
# from .models import Client, ClientCommunication
# from rest_framework import serializers

# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = '__all__'
        
# class ClientCommunicationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClientCommunication
#         fields = '__all__'