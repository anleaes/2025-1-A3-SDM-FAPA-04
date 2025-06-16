from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'communicationchannels'

router = routers.DefaultRouter()
router.register('', views.CommunicationchannelsViewSet, basename='canais_de_comunicação')

urlpatterns = [
    path('', include(router.urls) )
]
