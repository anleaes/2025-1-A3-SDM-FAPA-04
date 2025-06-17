from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'contracts'

router = routers.DefaultRouter()
router.register('', views.ContractViewSet, basename='contratos')

urlpatterns = [
    path('', include(router.urls) )
]

