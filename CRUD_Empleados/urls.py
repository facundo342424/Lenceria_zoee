# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('',listaEmpleados,name='listaEmpleados'),
    path('Guardar_empleado/', Guardar_empleado, name='Guardar_empleado'),
    path('borrar_empl/<int:id_Empleado>/', borrar_empl, name='borrar_empl'),
    path('editar/<int:id_Empleado>/', editar, name='editar'),
    path('edicion/<int:Empleado>/', edicion, name='edicion'),



]


