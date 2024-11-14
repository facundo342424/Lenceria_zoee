from django.db import models


class Clientes(models.Model):
    id_Cliente = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Domicilio = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=15)  # Changed to CharField for phone number
    
    class Meta:
        managed = False
        db_table = 'Clientes'