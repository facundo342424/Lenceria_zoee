# Caja/urls.py

from django.urls import path
from .views import Inicio,Apertura_de_caja, Cierre

urlpatterns = [

    path('Inicio/',Inicio,name='inicio'),
    path('Apertura/', Apertura_de_caja, name='apertura_de_caja'),
    path('Cierre/', Cierre, name='cierre_de_caja'),

]
