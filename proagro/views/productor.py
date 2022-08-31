from rest_framework.viewsets import ModelViewSet
from proagro.serializers import ProductorSerializer, OcurredEventSerializer, TillageSerializer
from proagro.models import OcurredEvent, Productor, Tillage


class ProductorViewSet(ModelViewSet):
    queryset = Productor.objects.all()
    serializer_class = ProductorSerializer