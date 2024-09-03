from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Asegúrate de que esta vista esté definida
    # Agrega otras URLs aquí si es necesario
]

