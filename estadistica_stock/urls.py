from django.urls import path
from .views import *

urlpatterns = [

    path('', Control_stock, name='Control_stock'),   
    
]