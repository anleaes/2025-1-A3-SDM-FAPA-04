from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'media'

router = routers.DefaultRouter()
router.register('', views.MediaViewSet, basename='meios_comunicação_do_cliente')

urlpatterns = [
    path('', include(router.urls) )
]