
from django.urls import path
from .views import *
from . import views

urlpatterns = [

    path('', lista_productos, name='lista_productos'),  
    path('Guardar_producto/', Guardar_producto, name='Guardar_producto'),
    path('borrar_prod/<int:id_Producto>/', borrar_prod, name='borrar_prod'),
    path('edit_prod/<int:id_Producto>/', edit_prod, name='edit_prod'),
    path('edi_prod/<int:id_Producto>/', edi_prod, name='edi_prod'),

    path('productos_venta/', views.productos_venta, name='productos_venta'), 
    path('producto/<int:id_Producto>/', views.detalle_producto, name='producto_detalle'),  
    path('agregar_al_carrito/<int:id_Producto>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/borrar_prod_carrito/<int:id_Producto>', views.borrar_prod_carrito, name='borrar_prod_carrito'),
    path('carrito/limpiar/', views.limpiar_carrito, name='limpiar_carrito'),

    path('control_stock/', control_stock, name='control_stock'), 
    path('Añadir_stock/', Añadir_stock, name='Añadir_stock'),
    path('eliminar/<int:id_stock>/', eliminar, name='eliminar'),
    path('editar/<int:id_stock>/', editar, name='editar'),
    path('edicion/<int:id_stock>/', edicion, name='edicion'),

    
]



