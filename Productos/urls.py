# urls.py
# urls.py
from django.urls import path
from  .views import *

urlpatterns = [
    path('', lista, name='lista'),
    path('Guardar_producto/', Guardar_producto, name='Guardar_producto'),
    path('Eliminar_producto/<int:prod>/', Eliminar_producto, name='Eliminar_producto'),
    path('editar/<int:prod>/', editar, name='editar'),
]

