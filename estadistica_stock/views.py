import random
from random import randint
from django.shortcuts import render

def Control_stock(request):
    chartLabel = "Préstamos"
    etiquetas = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    meses = 12
    minimo = 10
    maximo = 100
    datos = []

    for i in range(meses):
        datos.append(randint(minimo, maximo))

    context = {
        "labels": etiquetas,
        "chartLabel": chartLabel,
        "data": datos,
    }

    return render(request, 'stock_estadistica.html', context)
