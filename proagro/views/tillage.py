from rest_framework.viewsets import ModelViewSet
from proagro.serializers import ProductorSerializer, OcurredEventSerializer, TillageSerializer
from proagro.models import OcurredEvent, Productor, Tillage


class TillageViewSet(ModelViewSet):
    queryset = Tillage.objects.all()
    serializer_class = TillageSerializer