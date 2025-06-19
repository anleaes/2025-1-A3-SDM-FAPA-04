from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('corpo_dos_contratos', include( 'bodycontracts.urls', namespace='bodycontracts')),
    path('clientes/', include('clients.urls', namespace='clients')),
    path('canais_de_comunicação_com_o_cliente/', include('communicationchannels.urls', namespace='clientcommunication')),
    path('contratos/', include('contracts.urls', namespace='contracts')),	
    path('tipos_de_contrato/', include('contracttypes.urls', namespace='contracttypes')),
    path('negociacao/', include('negotiations.urls', namespace='negotiations')),
]
