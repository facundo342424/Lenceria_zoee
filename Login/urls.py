from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('logout/', views.salir, name='salir'),
    path('perfil/', views.perfil, name='perfil'),
    path('register/', views.register, name='register'),
]
