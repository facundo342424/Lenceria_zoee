from django.urls import path
from . import views

urlpatterns = [
    path('', views.administrarCajas.as_view(), name="administrarCajas"), 
    path('abrirCaja/', views.abrirCaja, name="abrirCaja"),  
    #path('adminLTE/', views.lte, name="lte"),   
]
