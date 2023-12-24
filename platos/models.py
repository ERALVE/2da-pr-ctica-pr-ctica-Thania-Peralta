from django.db import models

class Platos(models.Model):
    nombre = models.CharField(max_length=25)
    precio = models.CharField(max_length=8, default='00000000')
    procedencia = models.CharField(max_length=25, default='Desconocido')


