# Generated by Django 4.2.4 on 2024-09-28 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_Productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='CRUD_Productos',  # Cambiado de 'productos' a 'CRUD_Productos'
            old_name='color_prod',
            new_name='Color',
        ),
        migrations.RenameField(
            model_name='CRUD_Productos',  # Cambiado de 'productos' a 'CRUD_Productos'
            old_name='marca_prod',
            new_name='Marca',
        ),
        migrations.RenameField(
            model_name='CRUD_Productos',  # Cambiado de 'productos' a 'CRUD_Productos'
            old_name='nombre_prod',
            new_name='Nombre',
        ),
        migrations.RenameField(
            model_name='CRUD_Productos',  # Cambiado de 'productos' a 'CRUD_Productos'
            old_name='precio_prod',
            new_name='Precio',
        ),
    ]

