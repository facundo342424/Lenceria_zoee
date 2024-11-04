from django.db import models
# Create your models here.
class Ventas(models.Model):
    id_Venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateField(null=True, blank=True)
    hora_venta = models.TimeField(null=True, blank=True)
    total_venta = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

   

    def __str__(self):
        return f'Ventas {self.id_Venta}'

    class Meta:
        db_table = 'Ventas'



