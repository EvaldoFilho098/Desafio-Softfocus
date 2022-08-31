from django.db import models


class Notification(models.Model):

    message = models.TextField()

    def __str__(self):
        return f"New Notification {self.id}" 