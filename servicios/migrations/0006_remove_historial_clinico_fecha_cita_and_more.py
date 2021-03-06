# Generated by Django 4.0 on 2022-05-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0005_historial_clinico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historial_clinico',
            name='fecha_cita',
        ),
        migrations.RemoveField(
            model_name='historial_clinico',
            name='motivo_cita',
        ),
        migrations.RemoveField(
            model_name='historial_clinico',
            name='nombre_veterinario',
        ),
        migrations.RemoveField(
            model_name='historial_clinico',
            name='tipo_cita',
        ),
        migrations.RemoveField(
            model_name='historial_clinico',
            name='paciente',
        ),
        migrations.AddField(
            model_name='historial_clinico',
            name='paciente',
            field=models.ManyToManyField(to='servicios.agendamiento_citas'),
        ),
    ]
