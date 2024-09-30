from django.db import models


class Proveedores(models.Model):
    id_Proveedor = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Telefono = models.DecimalField(max_digits=10, decimal_places=2)
    Correo_electronico = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Apellido= models.CharField(max_length=100)
     

   

    def __str__(self):
        return f'Proveedores {self.id_Proveedor}'

    class Meta:
        db_table = 'Proveedores'

# Create your models here.
