from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sistema.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('productos/', include('CRUD_Productos.urls')),
    path('proveedores/', include('CRUD_Proveedores.urls')),
]
