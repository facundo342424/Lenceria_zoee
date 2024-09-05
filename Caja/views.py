# Caja/views.py

# Caja/views.py
from django.shortcuts import render

def Apertura_de_caja(request):
    return render(request, 'Apertura_de_caja.html')

def Cierre(request):
    return render(request, 'Cierre.html')



