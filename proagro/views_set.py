from rest_framework.viewsets import ModelViewSet
from .serializers import ProductorSerializer, OcurredEventSerializer, TillageSerializer
from .models import OcurredEvent, Productor, Tillage

class ProductorViewSet(ModelViewSet):
    queryset = Productor.objects.all()
    serializer_class = ProductorSerializer


class OcurredEventViewSet(ModelViewSet):
    queryset = OcurredEvent.objects.all()
    serializer_class = OcurredEventSerializer


class TillageViewSet(ModelViewSet):
    queryset = Tillage.objects.all()
    serializer_class = TillageSerializer