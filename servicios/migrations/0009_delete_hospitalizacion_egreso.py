# Generated by Django 4.0 on 2022-05-23 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0008_alter_carton_vacuna_fecha_vacuna'),
    ]

    operations = [
        migrations.DeleteModel(
            name='hospitalizacion_egreso',
        ),
    ]