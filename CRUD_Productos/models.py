from django.db import models


class Productos(models.Model):
    id_Producto = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Marca= models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Color = models.CharField(max_length=50)

   

    def __str__(self):
        return f'Productos {self.id_Producto}'

    class Meta:
        db_table = 'Productos'



# Create your models here.
