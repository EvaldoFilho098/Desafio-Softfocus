from rest_framework.serializers import ModelSerializer
from .models import OcurredEvent, Productor, Tillage


class ProductorSerializer(ModelSerializer):
    class Meta:
        model = Productor
        fields = ['id', 'name', 'email', 'cpf']


class OcurredEventSerializer(ModelSerializer):
    class Meta:
        model = OcurredEvent
        fields = ['id', 'type', 'date']


class TillageSerializer(ModelSerializer):
    class Meta:
        model = Tillage
        fields = ['id', 'latitude', 'longitude', 'tillage_type', 'harvest_date']


