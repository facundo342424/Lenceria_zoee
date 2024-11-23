# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('empleados/',empleados,name='empleados'),
    path('Añadir_empleado/', Añadir_empleado, name='Añadir_empleado'),
    path('borrar_empleado/<int:id_Empleado>/', borrar_empleado, name='borrar_empleado'),
    path('editar/<int:id_Empleado>/', editar, name='editar'),
    path('edicion/<int:id_Empleado>/', edicion, name='edicion'),
    



]

