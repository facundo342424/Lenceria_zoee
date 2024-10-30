from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import empleados
from django.contrib import messages

def listaEmpleados(request):
    empleado_lista = empleados.objects.all()
    valor = {
        'empleado_lista': empleado_lista
    }
    return render(request, 'listaEmpleados.html', valor)

def Guardar_empleado(request):
    if request.method == 'POST':
        Nombre = request.POST['Nombre']
        Apellido = request.POST['Apellido']
        Telefono = request.POST['Telefono']
        correo_electronico = request.POST['correo_electronico']
        DNI = request.POST['DNI']
        Dirección = request.POST['Dirección']
        Localidad = request.POST['Localidad']

        
        empleado = empleados(Nombre=Nombre, Apellido=Apellido,Telefono=Telefono, correo_electronico=correo_electronico,DNI=DNI,Dirección=Dirección,Localidad=Localidad)
        empleado.save()
        messages.success(request, '¡Empleado guardado con éxito!')
        
       
        return redirect('listaEmpleados')
    
   
    return redirect('listaEmpleados')

def borrar_empl(request, id_Empleado):
    empleado = empleados.objects.get(id_Empleado=id_Empleado)
    empleado.delete()
    messages.info(request, 'Empleado eliminado')
   
    return redirect('listaEmpleados')

def editar(request, id_Empleado):
    editar_empleado = empleados.objects.get(id_Empleado=id_Empleado)  
    empleado_lista = empleados.objects.all()
    valor = {
        'editar_empleado': editar_empleado,
        'empleado_lista': empleado_lista,
    }
    return render(request, 'listaEmpleados.html', valor)

def edicion(request, id_Empleado):
    empleado = empleados.objects.get(id_Empleado=id_Empleado)
    if request.method == 'POST':
        empleado.Nombre = request.POST['Nombre']
        empleado.Apellido = request.POST['Apellido']
        empleado.Telefono = request.POST['Telefono']
        empleado.correo_electronico = request.POST['correo_electronico']
        empleado.DNI = request.POST['DNI']
        empleado.Dirección = request.POST['Dirección']
        empleado.Localidad = request.POST['Localidad']
        empleado.save()
        messages.success(request, 'Empleado actualizado con éxito')
        
        return redirect('listaEmpleados')

    return redirect('listaEmpleados')


    
    

