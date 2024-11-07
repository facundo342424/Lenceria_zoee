from django.contrib import admin
from CRUD_Carrito.models import caja

# Register your models here.
@admin.register(caja)
class cajaAdmin(admin.ModelAdmin):
    list_display = ["Fecha_apertura_caja","Fecha_cierre_caja","Monto_inicial_Caja","Total_ingresos_caja",'Total_egresos_caja','id_Empleado']
# Cambiar el nombre en la vista de lista en el administrador
caja._meta.verbose_name_plural = "Gestión de Ventas"

    