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
from loguinApp.views import CustomLoginView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ResgistrodeVentas.urls')),


 

    path('',include('CRUD_Productos.urls')),
    path('',include('CRUD_Clientes.urls')),
    path('',include('CRUD_Carrito.urls')),
  
    path('',include('CRUD_Proveedores.urls')),
  
    path('',include('loguinApp.urls')),
    
    
   
 
    

    
    
     
]