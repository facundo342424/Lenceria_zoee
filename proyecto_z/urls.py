"""
URL configuration for proyecto_z project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
 # proyecto_z/urls.py

from django.contrib import admin
from django.urls import path, include
from Productos.views import lista,formulario,borrar
from Caja.views import Inicio,Apertura_de_caja 
 # Importa la vista que quieres mostrar en la raíz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',lista,name='lista'),
    path('',formulario, name='formulario'),
    path('',borrar, name='borrar'),
    path('',Inicio, name='inicio'),# Ruta para la raíz
    path('',Apertura_de_caja, name='apertura_de_caja'),
    path('Productos/',include('Productos.urls')),
    path('caja/', include('Caja.urls')), 
    
    
     # Rutas de la aplicación Caja
]



