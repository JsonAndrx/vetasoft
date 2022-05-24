# Generated by Django 4.0.4 on 2022-05-19 21:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('servicios', '0002_receta_medica'),
    ]

    operations = [
        migrations.CreateModel(
            name='hospitalizacion_ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingreso', models.DateTimeField(default=datetime.datetime.now)),
                ('observatorio', models.CharField(max_length=250)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.pacientes')),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.veterinario')),
            ],
            options={
                'verbose_name': 'Hospitalizacion Ingreso',
            },
        ),
        migrations.CreateModel(
            name='hospitalizacion_egreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('egreso', models.DateTimeField(default=datetime.datetime.now)),
                ('observatorio', models.CharField(max_length=259)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.pacientes')),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.veterinario')),
            ],
            options={
                'verbose_name': 'Hospitalizacion Egreso',
            },
        ),
    ]
