from rest_framework import viewsets
from monteseupc.models import *
from .serializers import *

# Create your views here.

class MonteSeuPcViewSet(viewsets.ModelViewSet):
	queryset = MonteSeuPC.objects.all()
	serializer_class = MonteSeuPcSerializer

class ProcessadorViewSet(viewsets.ModelViewSet):
    queryset = Processador.objects.all()
    serializer_class = ProcessadorSerializer

class PlacaMaeViewSet(viewsets.ModelViewSet):
    queryset = PlacaMae.objects.all()
    serializer_class = PlacaMaeSerializer

class MemoriaViewSet(viewsets.ModelViewSet):
    queryset = Memoria.objects.all()
    serializer_class = MemoriaSerializer

class PlacaDeVideoViewSet(viewsets.ModelViewSet):
    queryset = PlacaDeVideo.objects.all()
    serializer_class = PlacaDeVideoSerializer