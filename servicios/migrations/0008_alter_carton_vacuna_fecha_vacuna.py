# Generated by Django 4.0 on 2022-05-23 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0007_delete_historial_clinico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carton_vacuna',
            name='fecha_vacuna',
            field=models.DateField(),
        ),
    ]
