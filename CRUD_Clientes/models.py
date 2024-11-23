from django.db import models

# Create your models here.
class Clientes(models.Model):
    id_Cliente = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Domicilio =models.CharField(max_length=100)
    Telefono = models.DecimalField(max_digits=15, decimal_places=2)
   
    
    class Meta:
        db_table = 'Clientess'

