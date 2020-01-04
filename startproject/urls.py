"""startproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from monteseupc.views import *
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'api/monteseupc', MonteSeuPcViewSet)
router.register(r'api/processadores', ProcessadorViewSet)
router.register(r'api/placamaes', PlacaMaeViewSet)
router.register(r'api/memorias', MemoriaViewSet)
router.register(r'api/placasdevideo', PlacaDeVideoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include(router.urls)),
]
