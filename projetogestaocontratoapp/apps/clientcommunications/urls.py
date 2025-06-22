from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'clientcommunications'

router = routers.DefaultRouter()
router.register('', views.ClientCommunicationViewSet, basename='canais_de_comunicação_com_o_cliente')

urlpatterns = [
    path('', include(router.urls) )
]
