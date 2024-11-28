from django.urls import path
from .views import Cajas,Apertura_de_caja, Cierre

urlpatterns = [

    path('Cajas/',Cajas,name='Cajas'),
    path('', Apertura_de_caja, name='apertura_de_caja'),
    path('', Cierre, name='cierre_de_caja'),
    #forloop.counter

]
