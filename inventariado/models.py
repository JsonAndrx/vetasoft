from django.db import models
from usuarios.models import tipo_mascota
import datetime
# Create your models here.

class vacunas(models.Model):
    nombre_vacuna = models.CharField(max_length=45, blank=False, unique=True)
    vacuna_cantidad = models.IntegerField(null=False)
    vacuna_animal = models.ForeignKey(tipo_mascota, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Vacuna"

    def __str__(self):
        return self.nombre_vacuna


class medicina(models.Model):
    nombre_medicina = models.CharField(max_length=45, blank=False, unique=True)
    medicina_cantidad = models.IntegerField(null=False)
    medicina_animal = models.ForeignKey(tipo_mascota, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Medicina"

    def __str__(self):
        return self.nombre_medicina

    
class inventario(models.Model):
    medicina = models.ForeignKey(medicina, on_delete=models.CASCADE)
    cantidad_medicina = models.IntegerField(null=False)
    vacuna = models.ForeignKey(vacunas, on_delete=models.CASCADE)
    cantidad_vacuna = models.IntegerField(null=False)
    inventario_fecha = models.DateField(blank=False)