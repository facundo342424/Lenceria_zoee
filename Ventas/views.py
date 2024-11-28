from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ventas

def venta_lista(request):
    ventas_lista = Ventas.objects.all()  
    return render(request, 'ventas.html', {'ventas_lista': ventas_lista}) 
def Añadir_venta(request):
    if request.method == 'POST':
        Fecha_venta = request.POST['Fecha_venta']
        Total_venta = request.POST['Total_venta']
        Nombre_de_tipo_de_venta = request.POST['Nombre_de_tipo_de_venta']
        Descripción = request.POST['Descripción']
        Dni = request.POST['Dni']
        Nombre = request.POST['Nombre']



        if Ventas.objects.filter(Fecha_venta=Fecha_venta, Total_venta=Total_venta, Nombre_de_tipo_de_venta=Nombre_de_tipo_de_venta, Descripción=Descripción, Dni=Dni,Nombre=Nombre).exists():
            messages.error(request, 'Este producto ya existe.')
        else:
            venta = Ventas(Fecha_venta=Fecha_venta, Total_venta=Total_venta, Nombre_de_tipo_de_venta=Nombre_de_tipo_de_venta, Descripción=Descripción, Dni=Dni,Nombre=Nombre)
            venta.save()


            messages.success(request, '¡Venta añadida!')
            return redirect('venta_lista')

    return render(request, 'ventas.html')


def borrar_venta(request,id_Venta ):
    venta = Ventas.objects.get(id_Venta=id_Venta)
    venta.delete()
    messages.info(request, 'Venta eliminada')
    return redirect('venta_lista')

def edit_venta(request, id_Venta):
    edita_venta = Ventas.objects.get(id_Venta=id_Venta)  

    ventas_lista = Ventas.objects.all()
    valor = {
        'edita_venta': edita_venta,
        'ventas_lista': ventas_lista
    }
    return render(request, 'ventas.html', valor)

def edi_venta(request, id_Venta):
    venta = Ventas.objects.get(id_Venta=id_Venta)
    if request.method == 'POST':
        venta.fecha_venta = request.POST['fecha_venta']
        venta.total_venta = request.POST['total_venta']
        venta.Nombre_de_tipo_de_venta = request.POST['Nombre_de_tipo_de_venta']
        venta.Descripción = request.POST['Descripción']
        venta.Dni = request.POST['Dni']
        venta.Nombre = request.POST['Nombre']
        venta.save()
        messages.success(request, 'Producto actualizado con éxito')
        
        
        return redirect('venta_lista')

    return redirect('venta_lista')


