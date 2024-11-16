from django.db import models

class Productos(models.Model):
    id_Producto = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Marca = models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Color = models.CharField(max_length=100)
    Cantidad = models.DecimalField(max_digits=100, decimal_places=2)
    


    class Meta:
        db_table = 'productos'


class Stock(models.Model):
    id_stock = models.BigAutoField(db_column='id_stock', primary_key=True)
    id_Producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_Producto')
    Descripción = models.CharField(max_length=200)
    Talle = models.CharField(max_length=200)
    Genero = models.CharField(max_length=100)
    Color = models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=30, decimal_places=2)
    Cantidad = models.DecimalField(max_digits=20, decimal_places=2)
 
    class Meta:
        managed = False
        db_table = 'stock'


