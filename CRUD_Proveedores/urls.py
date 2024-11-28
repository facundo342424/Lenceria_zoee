from django.urls import path
from .views import *

urlpatterns = [
    path('',proveedores,name='proveedores'),
    path('Guardar_proveedor/', Guardar_proveedor, name='Guardar_proveedor'),
    path('borrar_prov/<int:id_Proveedor>/', borrar_prov, name='borrar_prov'),
    path('editar/<int:id_Proveedor>/', editar, name='editar'),
    path('edicion/<int:id_Proveedor>/', edicion, name='edicion'),
    



]
