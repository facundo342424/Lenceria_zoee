from django.urls import path
from . import views

urlpatterns = [
    # Aquí van tus rutas, por ejemplo:
    path('abrir_caja/', views.abrir_caja, name='abrir_caja'),
    # Agrega otras rutas necesarias
]
