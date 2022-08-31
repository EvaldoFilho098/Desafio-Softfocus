from django.db import models


class Productor(models.Model):

    name = models.CharField(max_length=128)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.name