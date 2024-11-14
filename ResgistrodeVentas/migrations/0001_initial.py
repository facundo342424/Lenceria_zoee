# Generated by Django 4.2.4 on 2024-11-13 17:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_Producto', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Marca', models.CharField(max_length=100)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Color', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='TipodeVenta',
            fields=[
                ('id_TipoVenta', models.BigAutoField(db_column='id_TipoVenta', primary_key=True, serialize=False)),
                ('Nombre_de_tipo_de_venta', models.CharField(db_column='Nombre_de_tipo_de_venta', max_length=191)),
                ('Descripción', models.CharField(db_column='Descripción', max_length=191)),
                ('Fecha_Creación', models.DateTimeField(db_column='Fecha_Creación')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'TipodeVenta',
            },
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_Venta', models.BigAutoField(db_column='id_Venta', primary_key=True, serialize=False)),
                ('fecha_venta', models.DateTimeField(db_column='fecha_venta')),
                ('hora_venta', models.TimeField(db_column='hora_venta', default=django.utils.timezone.now)),
                ('total_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_TipoVenta', models.ForeignKey(db_column='id_TipoVenta', on_delete=django.db.models.deletion.DO_NOTHING, to='ResgistrodeVentas.tipodeventa')),
            ],
            options={
                'db_table': 'ventas',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id_detalle_venta', models.BigAutoField(db_column='id_detalle_venta', primary_key=True, serialize=False)),
                ('cantidad_de_productos_detalle_de_ventas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_unitario_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_Producto', models.ForeignKey(db_column='id_Producto', on_delete=django.db.models.deletion.DO_NOTHING, to='ResgistrodeVentas.productos')),
                ('id_Venta', models.ForeignKey(db_column='id_Venta', on_delete=django.db.models.deletion.DO_NOTHING, to='ResgistrodeVentas.ventas')),
            ],
            options={
                'db_table': 'detalleVenta',
            },
        ),
    ]
