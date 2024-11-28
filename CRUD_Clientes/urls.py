
from django.urls import path
from .views import *

urlpatterns = [
    path('',clientes,name='clientes'),
    path('Añadir_cliente/', Añadir_cliente, name='Añadir_cliente'),
    path('borrar_cliente/<int:id_Cliente>/', borrar_cliente, name='borrar_cliente'),
    path('editar/<int:id_Cliente>/', editar, name='editar'),
    path('edicion/<int:id_Cliente>/', edicion, name='edicion'),
    



]
