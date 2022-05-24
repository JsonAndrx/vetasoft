from django.contrib import admin
from .models import vacunas, medicina, inventario
# Register your models here.

admin.site.register(vacunas)
admin.site.register(medicina)
admin.site.register(inventario)