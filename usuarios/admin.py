from django.contrib import admin
from .models import tipo_mascota, mascota_sexo, pacientes, tipo_documento, propietario, veterinario

# Register your models here.

admin.site.register(tipo_mascota)
admin.site.register(mascota_sexo)
admin.site.register(pacientes)
admin.site.register(tipo_documento)
admin.site.register(propietario)
admin.site.register(veterinario)