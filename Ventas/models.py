from django.db import models
from django.utils import timezone

class TipodeVenta(models.Model):
    id_TipoVenta = models.BigAutoField(db_column='id_TipoVenta', primary_key=True)
    Nombre_de_tipo_de_venta = models.CharField(db_column='Nombre_de_tipo_de_venta', max_length=191)
    Descripción = models.CharField(db_column='Descripción', max_length=191)
    Fecha_Creación = models.DateTimeField(db_column='Fecha_Creación')  
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_ventas'

    def __str__(self):
        return f"{self.Nombre_de_tipo_de_venta,self.Descripción} "

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
        managed = False
        db_table = 'empleados'

    def __str__(self):
        return f"{self.Dni} "


class Clientes(models.Model):
    id_Cliente = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Domicilio =models.CharField(max_length=100)
    Telefono = models.DecimalField(max_digits=15, decimal_places=2)
   
    
    class Meta:
        managed = False
        db_table = 'Clientes'
    def __str__(self):
        return f"{self.Nombre} "





class Ventas(models.Model):
    id_Venta = models.BigAutoField(db_column='id_Venta', primary_key=True)  # Field name made lowercase.
    id_Empleado = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='id_Empleado',null=True)
    id_Cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_Cliente')
    id_TipoVenta = models.ForeignKey(TipodeVenta, models.DO_NOTHING, db_column='id_TipoVenta')
    Fecha_venta = models.DateTimeField()
    Total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = 'Ventas'
    def __str__(self):
        return f"{self.Nombre_de_tipo_de_venta,self.Descripción,self.Dni,self.Nombre} "

