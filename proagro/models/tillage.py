from django.db import models


class Tillage(models.Model):

    latitude = models.FloatField()
    longitude = models.FloatField()
    tillage_type = models.CharField(max_length=32)
    harvest_date = models.DateField()
    productor = models.ForeignKey("Productor", on_delete = models.CASCADE, related_name = "tillages")

    def __str__(self):
        return "{} - {}".format(self.tillage_type, self.harvest_date.strftime("%d/%m/%Y"))