from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'orders'

router = routers.DefaultRouter()
router.register('', views.OrderViewSet, basename='negociacao')
router.register('', views.ContractVersionViewSet, basename='Versoes_Contratos')

urlpatterns = [
    path('', include(router.urls) )
]
