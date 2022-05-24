from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class tipo_mascota(models.Model):
    tipo_mascota = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        verbose_name = "Tipo mascota"
        verbose_name_plural = "Tipo mascotas"

    def __str__(self):
        return self.tipo_mascota

class mascota_sexo(models.Model):
    sexo_mascota = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        verbose_name = "Mascota sexo"
        verbose_name_plural = "Mascota sexos"

    def __str__(self):
        return self.sexo_mascota

class pacientes(models.Model):
    nombre = models.CharField(max_length=45, blank=False)
    tipo_mascota = models.ForeignKey(tipo_mascota, on_delete=models.CASCADE)
    sexo_mascota = models.ForeignKey(mascota_sexo, on_delete=models.CASCADE)
    raza = models.CharField(max_length=45, blank=False)
    fecha_nacimiente = models.DateField(blank=False)
    mascota_color = models.CharField(max_length=20, blank=False)
    mascota_longitud = models.CharField(max_length=20, blank=False)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.nombre


class tipo_documento(models.Model):
    tipo_documento = models.CharField(max_length=25, blank=False, unique=True)

    class Meta:
        verbose_name = "Tipo documento"
        verbose_name_plural = "Tipo documentos"

    def __str__(self):
        return self.tipo_documento

class propietario(models.Model):
    nombre_propietario = models.CharField(max_length=45, blank=False)
    paciente = models.ForeignKey(pacientes, on_delete=models.CASCADE)
    tipo_documento = models.ForeignKey(tipo_documento, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=10, blank=False, unique=True, validators=[RegexValidator(r'^\d{1,10}$')])
    direccion_propietario = models.CharField(max_length=45, blank=False)
    celular_propietario = models.CharField(max_length=10, blank=False, unique=True, validators=[RegexValidator(r'^\d{1,10}$')] )
    email_propietario = models.EmailField(max_length=45, blank=False, unique=True)

    class Meta:
        verbose_name = "Propietario"
        verbose_name_plural = "Propietarios"

    def __str__(self):
        return self.nombre_propietario


class veterinario(models.Model):
    nombre_veterinario = models.CharField(max_length=45, blank=False)
    especializacion = models.CharField(max_length=45, blank=False)
    documento = models.ForeignKey(tipo_documento, on_delete=models.CASCADE)
    numero_documento= models.CharField(max_length=10, blank=False, unique=True, validators=[RegexValidator(r'^\d{1,10}$')])

    class Meta:
        verbose_name ="Veterinario"

    def __str__(self):
        return self.nombre_veterinario