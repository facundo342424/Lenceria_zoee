from django.shortcuts import render

def Cajas(request):
    return render(request,'cajas.html')

def Apertura_de_caja(request):
    return render(request, 'Apertura_de_caja.html')


def Cierre(request):
    return render(request, 'Cierre.html')




