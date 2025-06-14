from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'negotiation'

router = routers.DefaultRouter()
router.register('', views.NegotiationViewSet, basename='negociacao')
router.register('', views.ContractVersionViewSet, basename='Versoes_Contratos')

urlpatterns = [
    path('', include(router.urls) )
]
