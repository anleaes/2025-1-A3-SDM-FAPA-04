from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'bodycontracts'

router = routers.DefaultRouter()
router.register('', views.BodyContractViewSet, basename='Corpo_contratos')

urlpatterns = [
    path('', include(router.urls) )
]
