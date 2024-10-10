from django.db import models


class empleados(models.Model):
    id_Empleado= models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido= models.CharField(max_length=100)
    Telefono = models.DecimalField(max_digits=10, decimal_places=2)
    correo_electronico= models.CharField(max_length=50)
    DNI = models.DecimalField(max_digits=10, decimal_places=2)
    Direccion= models.CharField(max_length=100)
    Localidad= models.CharField(max_length=100)

    def __str__(self):
        return f'empleados {self.id_Empleado}'

    class Meta:
        db_table = 'empleados'



# Create your models here.

