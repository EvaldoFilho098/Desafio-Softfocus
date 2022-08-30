from django.contrib import admin
from .models import Productor, Tillage, OcurredEvent


@admin.register(Productor, Tillage, OcurredEvent)
class ProagroAdmin(admin.ModelAdmin):
    ...
