# urls.py
# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', lista, name='lista'),
    path('',productos,name='productos'),
    path('Guardar_producto/', Guardar_producto, name='Guardar_producto'),
    path('borrar_prod/<int:id_Producto>/', borrar_prod, name='borrar_prod'),
    path('editar/<int:id_Producto>/', editar, name='editar'),
    path('edicion/<int:id_Producto>/', edicion, name='edicion'),
    path('',productos,name='productos'),



]


