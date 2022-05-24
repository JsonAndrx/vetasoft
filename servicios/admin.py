from django.contrib import admin
from .models import carton_vacuna, tipo_cita, agendamiento_citas, receta_medica, hospitalizacion
carton_vacuna
# Register your models here.

admin.site.register(tipo_cita)
admin.site.register(agendamiento_citas)
admin.site.register(receta_medica)
admin.site.register(hospitalizacion)
admin.site.register(carton_vacuna)
