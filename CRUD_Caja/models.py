from django.db import models


# Create your models here.
from django.db import models

class Caja(models.Model):
    id_caja = models.AutoField(primary_key=True)
    id_empleado = models.IntegerField()
    id_factura = models.IntegerField()
    fecha_apertura_caja = models.DateField()
    fecha_cierre_caja = models.DateField()
    monto_inicial_caja = models.DecimalField(max_digits=10, decimal_places=0)
    total_ingresos_caja = models.DecimalField(max_digits=10, decimal_places=0)
    total_egresos_caja = models.DecimalField(max_digits=10, decimal_places=0)
    total_caja = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f'Caja {self.id_caja}'

    class Meta:
        db_table = 'caja'

    
