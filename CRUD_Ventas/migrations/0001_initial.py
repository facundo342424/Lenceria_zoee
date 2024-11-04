# Generated by Django 4.2.4 on 2024-11-03 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_Venta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField(blank=True, null=True)),
                ('hora_venta', models.TimeField(blank=True, null=True)),
                ('total_venta', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
            options={
                'db_table': 'Ventas',
            },
        ),
    ]
