from django.urls import path
from .views import *

urlpatterns = [

    path('', venta_lista, name='venta_lista'),   
    path('Añadir_venta/', Añadir_venta, name='Añadir_venta'),
    path('borrar_venta/<int:id_Venta>/', borrar_venta, name='borrar_venta'),
    path('edit_venta/<int:id_Venta>/', edit_venta, name='edit_venta'),
    path('edi_venta/<int:id_Venta>/', edi_venta, name='edi_venta'),
]