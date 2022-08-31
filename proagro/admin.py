from django.contrib import admin
from .models import Productor, Tillage, OcurredEvent, Notification


@admin.register(Productor, Tillage, OcurredEvent, Notification)
class ProagroAdmin(admin.ModelAdmin):
    ...
