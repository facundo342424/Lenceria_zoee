# Caja/views.py

# Caja/views.py

from django.shortcuts import render
from .models import Caja

def Apertura_de_caja(request):
    cajas = Caja.objects.filter(fecha_cierre_caja__isnull=True)
    return render(request, 'Apertura_de_caja', {'cajas': cajas})

def Cierre(request):
    cajas = Caja.objects.filter(fecha_cierre_caja__isnull=False)
    return render(request, 'Cierre.html', {'cajas': cajas})



