from django.db import models
from usuarios.models import pacientes, veterinario
from inventariado.models import medicina, vacunas
import datetime
# Create your models here.

class tipo_cita(models.Model):
    tipo_cita = models.CharField(max_length=45, blank=False, unique=True)

    class Meta:
        verbose_name="Tipo Cita"

    def __str__(self):
        return self.tipo_cita

class agendamiento_citas(models.Model):
    paciente = models.ForeignKey(pacientes,  on_delete=models.CASCADE)
    tipo_cita = models.ForeignKey(tipo_cita, on_delete=models.CASCADE)
    fecha_cita = models.DateField(blank=False)
    motivo_cita = models.CharField(max_length=120)
    nombre_veterinario = models.ForeignKey(veterinario, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Agendamiento Cita"

    def __str__(self):
        return "%s" % (self.paciente)


class receta_medica(models.Model):
    paciente = models.ForeignKey(agendamiento_citas, on_delete=models.CASCADE)
    medicina = models.ForeignKey(medicina, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=250, blank=False)

    class Meta:
        verbose_name = "Receta Medica"

    def __str__(self):
        return "%s" % (self.paciente)


class hospitalizacion(models.Model):
    paciente = models.ForeignKey(pacientes, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(veterinario, on_delete=models.CASCADE)
    ingreso = models.DateTimeField(default=datetime.datetime.now)
    egreso = models.DateField(blank=True, null=True)
    observatorio = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Hospitalizacion"

    def __str__(self):
        return "%s" % (self.paciente)



class carton_vacuna(models.Model):
    paciente = models.ForeignKey(pacientes, on_delete=models.CASCADE)
    vacuna = models.ForeignKey(vacunas, on_delete=models.CASCADE)
    fecha_vacuna = models.DateField(blank=False)
    
    class Meta:
        verbose_name = "Carton Vacunas"

    def __str__(self):
        return "%s %s" % (self.vacuna, self.paciente)




