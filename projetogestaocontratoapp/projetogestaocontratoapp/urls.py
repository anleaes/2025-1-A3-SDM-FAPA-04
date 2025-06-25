from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home_view, name='home'),
    path("corpo_dos_contratos/", include( "bodycontracts.urls", namespace="bodycontracts")),
    path("clientes/", include( "clients.urls", namespace="clients")),
    path("canais_de_comunicação_com_o_cliente/", include( "clientcommunications.urls", namespace="clientcommunications")),
    path("canais_de_comunicação/", include( "communicationchannels.urls", namespace="communicationchannels")),
    path("contratos/", include( "contracts.urls", namespace="contracts")),	
    path("tipos_de_contrato/", include( "contracttypes.urls", namespace="contracttypes")),
    path("negociação/", include( "negotiations.urls", namespace="negotiations")),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
