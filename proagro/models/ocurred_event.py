from django.db import models
from proagro.utils import distance
from .notification import Notification


class OcurredEvent(models.Model):

    EVENTS_TYPE = (
        ("EXCESSIVE_RAIN", "CHUVA EXCESSIVA"),
        ("FROST", "GEADA"),
        ("HAIL", "GRANIZO"),
        ("DRY", "SECA"),
        ("GALE", "VENDAVAL"),
        ("LIGHTNING", "RAIO")
    )

    type = models.CharField(choices=EVENTS_TYPE, max_length=15)
    date = models.DateField()
    tillage = models.ForeignKey("Tillage", on_delete = models.CASCADE, related_name = "events")

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.type, self.date.strftime("%d/%m/%Y"))


    def save(self):
        
        events_on_day = OcurredEvent.objects.filter(date = self.date).exclude(type = self.type)

        for event in events_on_day:
            dist = distance(
                event.tillage.latitude, 
                event.tillage.longitude, 
                self.tillage.latitude, 
                self.tillage.longitude
                )
            
            if dist <= 10 :
                notification = Notification(message=f"""
                    Novo Evento detectado em um raio de {dist} km
                    Evento atual: {repr(self)} 
                    Evento anterior: {repr(event)}
                """
                )
                notification.save()
            
        super().save()