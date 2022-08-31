from rest_framework.viewsets import ModelViewSet
from proagro.serializers import ProductorSerializer, OcurredEventSerializer, TillageSerializer
from proagro.models import OcurredEvent, Productor, Tillage


class OcurredEventViewSet(ModelViewSet):
    queryset = OcurredEvent.objects.all()
    serializer_class = OcurredEventSerializer

    """
    def create(self, request, *args, **kwargs):
        ocurred_event = self.get_serializer(data=request.data)
        ocurred_event.is_valid(raise_exception=True)
        events_on_day = OcurredEvent.objects.filter(date = ocurred_event.date)
        self.perform_create(ocurred_event)
        headers = self.get_success_headers(ocurred_event.data)
        return Response(ocurred_event.data, status=status.HTTP_201_CREATED, headers=headers)
    """