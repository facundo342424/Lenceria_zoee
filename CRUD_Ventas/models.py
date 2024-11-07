from django.db import models
from django.utils import timezone
class Ventas(models.Model):
    id_Venta = models.BigAutoField(db_column='id_Venta', primary_key=True)  
    fecha_venta = models.DateTimeField(db_column='fecha_venta') 
    hora_venta = models.TimeField(db_column='hora_venta', default=timezone.now) 
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f'Ventas {self.id_Venta}'

    class Meta:
        db_table = 'Ventas'

