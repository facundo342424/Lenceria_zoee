from django.urls import path
from.views import *

 # Importa la vista que quieres mostrar en la raíz

urlpatterns = [
    path('',listaprov,name='listaprov'),

    
   
]