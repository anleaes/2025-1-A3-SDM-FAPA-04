from .models import BodyContract
from rest_framework import serializers
    
class BodyContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyContract
        fields = '__all__'