from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'negotiations'

router = routers.DefaultRouter()
router.register('', views.NegotiationViewSet, basename='negociacões')


urlpatterns = [
    path('', include(router.urls) )
]
