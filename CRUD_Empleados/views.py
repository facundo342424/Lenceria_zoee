from django.shortcuts import render, redirect
from Ventas.models import Empleados
from django.contrib import messages

def empleados(request):
    empleado_lista = Empleados.objects.all()
    valor = {
        'empleado_lista': empleado_lista
    }
    return render(request, 'lista_empleados.html', valor)

def Añadir_empleado(request):
    if request.method == 'POST':
        Nombre = request.POST['Nombre']
        Apellido = request.POST['Apellido']
        Telefono = request.POST['Telefono']
        Correo = request.POST['Correo']  
        Dni = request.POST['Dni']
        Dirección = request.POST['Dirección']
        Localidad = request.POST['Localidad']
        empleado = Empleados(Nombre=Nombre, Apellido=Apellido, Telefono=Telefono, Correo=Correo,Dni=Dni,Dirección=Dirección,Localidad=Localidad)
        empleado.save()
        messages.success(request, '¡Empleado añadido!')

        
       
        return redirect('empleados')
    
   
    return redirect('empleados')

def borrar_empleado(request, id_Empleado):
    empleado = Empleados.objects.get(id_Empleado=id_Empleado)
    empleado.delete()
    messages.info(request, 'Empleado eliminado')
   
    return redirect('empleados')

def editar(request, id_Empleado):
    editar_empleado = Empleados.objects.get(id_Empleado=id_Empleado)  
    empleado_lista = Empleados.objects.all()
    valor = {
        'editar_empleado': editar_empleado,
        'empleado_lista': empleado_lista
    }
    return render(request, 'lista.empleados', valor)

def edicion(request, id_Empleado):
    empleado = Empleados.objects.get(id_Empleado=id_Empleado)
    if request.method == 'POST':
        empleado.Nombre = request.POST['Nombre']
        empleado.Apellido = request.POST['Apellido']
        empleado.Telefono = request.POST['Telefono']
        empleado.Correo = request.POST['Correo']
        empleado.Dni = request.POST['Dni']
        empleado.Dirección = request.POST['Dirección']
        empleado.Localidad = request.POST['Localidad']
        empleado.save()
        messages.success(request, 'Empleado actualizado con éxito')

        
        return redirect('empleados')

    return redirect('empleados')



