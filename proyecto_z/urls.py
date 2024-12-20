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
from django.urls import path
from django.urls.conf import include



urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('Loginz.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('lista/',include('CRUD_Productos.urls')),
    path('empleados/',include('CRUD_Empleados.urls')),
    path('lista_user/',include('CRUD_Users.urls')),
    path('proveedores/',include('CRUD_Proveedores.urls')),
    path('clientes/',include('CRUD_Clientes.urls')),
    path('lista_ventas/',include('Ventas.urls')),
    path('Control_stock/',include('estadistica_stock.urls')),
    path('Control_producto/',include('producto_estadistica.urls')),
    

    
    

    
    

]
      
     
