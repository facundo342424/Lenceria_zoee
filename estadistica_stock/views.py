import random
from random import randint
from django.shortcuts import render

def Control_stock(request):
    chartLabel = "Préstamos"
    etiquetas = ['Buzo', 'Pantalón', 'Buz_overzide']  # Etiquetas específicas de los productos
    minimo = 10
    maximo = 100

    # Generar datos aleatorios para cada producto
    datos = [randint(minimo, maximo) for _ in etiquetas]

    context = {
        "labels": etiquetas,       # Los nombres de los productos aparecerán en la gráfica
        "chartLabel": chartLabel,  # Título de la gráfica
        "data": datos,             # Valores para cada producto
    }



    return render(request, 'stock_estadistica.html', context)
