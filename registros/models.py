# registros/models.py

from django.db import models


class Paciente(models.Model):
    id = models.AutoField(primary_key = True)
    nombre    = models.CharField(max_length = 50)
    direccion = models.CharField(max_length = 100)
    telefono  = models.CharField(max_length = 20)
    fecha_nacimiento = models.CharField(max_length = 15)
    edad      = models.CharField(max_length = 5)
    historial = models.TextField()

    search_field = ('id',)


    def __str__(self):
        return self.nombre

    @models.permalink
    def get_absolute_url(self):
        return ('paciente_detail', [self.pk])

class Medicamento(models.Model):
    nombre     = models.CharField(max_length = 30)
    tipo       = models.CharField(max_length = 30)
    indicacion = models.CharField(max_length = 30)

    def __str__(self):
        return self.nombre

    @models.permalink
    def get_absolute_url(self):
        return ('medicamento_detail', [self.pk])