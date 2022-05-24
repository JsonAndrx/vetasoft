# Generated by Django 4.0 on 2022-05-20 20:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('inventariado', '0001_initial'),
        ('servicios', '0003_hospitalizacion_ingreso_hospitalizacion_egreso'),
    ]

    operations = [
        migrations.CreateModel(
            name='carton_vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vacuna', models.DateTimeField(default=datetime.datetime.now)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.pacientes')),
                ('vacuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventariado.vacunas')),
            ],
            options={
                'verbose_name': 'Carton Vacunas',
            },
        ),
    ]