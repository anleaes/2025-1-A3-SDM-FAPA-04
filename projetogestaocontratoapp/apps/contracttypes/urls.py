from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'contracttypes'

router = routers.DefaultRouter()
router.register('', views.ContractTypeViewSet, basename='tipos_de_contrato')

urlpatterns = [
    path('', include(router.urls) )
]
