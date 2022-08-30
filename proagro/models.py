from django.db import models


class Productor(models.Model):

    name = models.CharField(max_length=128)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.name

class Tillage(models.Model):

    latitude = models.FloatField()
    longitude = models.FloatField()
    tillage_type = models.CharField(max_length=32)
    harvest_date = models.DateField()
    productor = models.ForeignKey(Productor, on_delete = models.CASCADE, related_name = "tillages")

    def __str__(self):
        return "{} - {}".format(self.tillage_type, self.harvest_date.strftime("%d/%m/%Y"))

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
    tillage = models.ForeignKey(Tillage, on_delete = models.CASCADE, related_name = "events")

    def __str__(self):
        return "{} - {}".format(self.type, self.date.strftime("%d/%m/%Y"))


