# urls.py
from django.urls import path
from .views import *

urlpatterns = [

    path('lista/', lista, name='lista'),   
    path('Guardar_producto/', Guardar_producto, name='Guardar_producto'),
    path('borrar_prod/<int:id_Producto>/', borrar_prod, name='borrar_prod'),
    path('editar_producto/<int:id_Producto>/', editar_producto, name='editar_producto'),
    path('edicion_producto/<int:id_Producto>/', edicion_producto, name='edicion_producto'),

    path('control/', control_stock, name='control_stock'), 
    path('Añadir_stock/', Añadir_stock, name='Añadir_stock'),
    path('eliminar/<int:id_stock>/', eliminar, name='eliminar'),
    path('editar/<int:id_stock>/', editar, name='editar'),
    path('edicion/<int:id_stock>/', edicion, name='edicion'),
]



