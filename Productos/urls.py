# urls.py
# urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('lista/',views.lista),
    path('lista_productos/',views.lista_Productos,name='lista_productos')
]
