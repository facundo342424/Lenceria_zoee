from django.urls import path
from .views import listaEmpleados, Añadir_empleados, borrar_empleado, editar, edicion

urlpatterns = [
    path('', listaEmpleados, name='listaEmpleados'),
    path('Añadir_empleados/', Añadir_empleados, name='Añadir_empleados'),
    path('borrar_empleado/<int:id_Empleado>/', borrar_empleado, name='borrar_empleado'),
    path('editar/<int:id_Empleado>/', editar, name='editar'),
    path('edicion/<int:id_Empleado>/', edicion, name='edicion'),
]
