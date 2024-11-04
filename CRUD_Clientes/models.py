from django.db import models

# Create your models here.
class Clientes(models.Model):
    id_Cliente = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Domicilio = models.CharField(max_length=100)
    Telefono = models.DecimalField(max_digits=10, decimal_places=2)
   

    def __str__(self):
        return f'Clientes {self.id_Cliente}'

    class Meta:
        db_table = 'Clientes'
