from django.db import models
class Empleados(models.Model):
    id_Empleado = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Telefono = models.DecimalField(max_digits=10, decimal_places=2)
    Correo = models.CharField(max_length=100)
    Dni = models.DecimalField(max_digits=10, decimal_places=2)
    Dirección =models.CharField(max_length=100)
    Localidad =models.CharField(max_length=100)

    
    class Meta:
        db_table = 'empleadoss'

