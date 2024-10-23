from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import empleados
from django.contrib import messages

def listaEmpleados(request):
    empleados_lista = empleados.objects.all()
    valor = {
        'empleados_lista': empleados_lista
    }
    return render(request, 'listaEmpleados.html', valor)

def Añadir_empleados(request):
    if request.method == 'POST':
        Nombre = request.POST['Nombre']
        Apellido = request.POST['Apellido']
        Telefono = request.POST['Telefono']
        correo_electronico = request.POST['correo_electronico']  
        dni = request.POST['DNI']
        Dirección = request.POST['Dirección']
        Localidad = request.POST['Localidad']
        
        empleado_instance = empleados(
            Nombre=Nombre, 
            Apellido=Apellido, 
            Telefono=Telefono, 
            correo_electronico=correo_electronico,
            DNI=dni,
            Dirección=Dirección,
            Localidad=Localidad,
        )
        empleado_instance.save()
        messages.success(request, 'Empleado añadido correctamente.')
        return redirect('listaEmpleados')  # Redirigir después de guardar

def borrar_empleado(request, id_Empleado):
    empleado_instance = empleados.objects.get(id_Empleado=id_Empleado)   
    empleado_instance.delete()
    messages.info(request, 'Empleado eliminado correctamente.')
    return redirect('listaEmpleados')

def editar(request, id_Empleado):
    editar_empleado = empleados.objects.get(id_Empleado=id_Empleado)
    empleados_lista = empleados.objects.all()
    valor = {
        'editar_empleado': editar_empleado, 
        'empleados_lista': empleados_lista
    }
    return render(request, 'listaEmpleados.html', valor)

def edicion(request, id_Empleado):
    empleado_instance = empleados.objects.get(id_Empleado=id_Empleado) 

    if request.method == 'POST':
        empleado_instance.Nombre = request.POST['Nombre']
        empleado_instance.Apellido = request.POST['Apellido']
        empleado_instance.Telefono = request.POST['Telefono']
        empleado_instance.correo_electronico = request.POST['correo_electronico']  
        empleado_instance.DNI = request.POST['DNI']
        empleado_instance.Dirección = request.POST['Dirección']
        empleado_instance.Localidad = request.POST['Localidad']
        empleado_instance.save()  
        messages.success(request, 'Empleado actualizado correctamente.')

    return redirect('listaEmpleados')



    
