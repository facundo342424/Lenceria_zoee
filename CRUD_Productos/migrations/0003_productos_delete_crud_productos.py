# Generated by Django 4.2.4 on 2024-09-29 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_Productos', '0002_rename_color_prod_productos_color_and_more'),
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
        migrations.DeleteModel(
            name='CRUD_Productos',
        ),
    ]
