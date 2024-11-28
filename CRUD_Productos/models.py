from django.db import models

class Productos(models.Model):
    id_Producto = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Marca = models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Color = models.CharField(max_length=100)
    Cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  

    class Meta:
        db_table = 'productos'

    def __str__(self):
        return f"{self.id_Producto}"


class Stock(models.Model):
    id_stock = models.BigAutoField(db_column='id_stock', primary_key=True)
    id_Producto = models.ForeignKey(Productos, on_delete=models.CASCADE, db_column='id_Producto')
    Descripción = models.CharField(max_length=200, blank=True, null=True)
    Talle = models.CharField(max_length=200, blank=True, null=True)
    Genero = models.CharField(max_length=100, blank=True, null=True)
    Color = models.CharField(max_length=100, blank=True, null=True)
    Precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default=0.00)
    Cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)

    class Meta:
        db_table = 'stock'

    def __str__(self):
        return f"{self.id_Producto.id_Producto}" 



