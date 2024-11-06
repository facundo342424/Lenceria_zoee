from django.urls import path
from .views import Tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, confirmar_pedido

urlpatterns = [
    path('tienda/', Tienda.as_view(), name='Tienda'),
    path('agregar_producto/<int:producto_id>/', agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('restar_producto/<int:producto_id>/', restar_producto, name='restar_producto'),
    path('limpiar_carrito/', limpiar_carrito, name='limpiar_carrito'),
    path('confirmar_pedido/', confirmar_pedido, name='confirmar_pedido'),
]
