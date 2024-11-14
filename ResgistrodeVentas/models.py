from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class TipodeVenta(models.Model):
    id_TipoVenta = models.BigAutoField(db_column='id_TipoVenta', primary_key=True)
    Nombre_de_tipo_de_venta = models.CharField(db_column='Nombre_de_tipo_de_venta', max_length=191)
    Descripción = models.CharField(db_column='Descripción', max_length=191)
    Fecha_Creación = models.DateTimeField(db_column='Fecha_Creación')  
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.Nombre_de_tipo_de_venta,self.Descripción} '

    class Meta:
        
        db_table = 'TipodeVenta'


class Productos(models.Model):
    id_Producto = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Marca = models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Color = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Nombre} '

    class Meta:
        db_table = 'Productos'


class Ventas(models.Model):
    id_Venta = models.BigAutoField(db_column='id_Venta', primary_key=True)  
    id_TipoVenta = models.ForeignKey(TipodeVenta, models.DO_NOTHING, db_column='id_TipoVenta')
    fecha_venta = models.DateTimeField(db_column='fecha_venta') 
    hora_venta = models.TimeField(db_column='hora_venta', default=timezone.now)  
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'{self.fecha_venta,self.hora_venta,self.total_venta} '
    class Meta:
    
        db_table = 'ventas'

class DetalleVenta(models.Model):
    id_detalle_venta = models.BigAutoField(db_column='id_detalle_venta', primary_key=True)  
    id_Producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_Producto')
    id_Venta = models.ForeignKey(Ventas, models.DO_NOTHING, db_column='id_Venta')
    cantidad_de_productos_detalle_de_ventas= models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario_venta= models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_venta= models.DecimalField(max_digits=10, decimal_places=2) 
    def __str__(self):
        return f'{self.cantidad_de_productos_detalle_de_ventas,self.precio_unitario_venta,self.subtotal_venta} '

    class Meta:
        
        db_table = 'detalleVenta'


