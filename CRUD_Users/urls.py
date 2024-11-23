from django.urls import path
from .views import *

urlpatterns = [

    path('lista_user', lista_user, name='lista_user'),   
    path('Guardar_user/', Guardar_user, name='Guardar_user'),
    path('borrar_user/<int:id_Usuario>/', borrar_user, name='borrar_user'),
    path('edit_user/<int:id_Usuario>/', edit_user, name='edit_user'),
    path('edi_user/<int:id_Usuario>/', edi_user, name='edi_user'),

]