from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users

def lista_user(request):
    user_lista = Users.objects.all()
    return render(request, 'lista_users.html', {'user_lista': user_lista})

def Guardar_user(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Contraseña = request.POST['Contraseña']
        Email = request.POST['Email']
        Dirección = request.POST['Dirección']

        if Users.objects.filter(Username=Username, Contraseña=Contraseña, Email=Email, Dirección=Dirección).exists():
            messages.error(request, 'Este user ya existe.')
        else:
            user = Users(Username=Username, Contraseña=Contraseña, Email=Email, Dirección=Dirección)
            user.save()
            messages.success(request, '¡user añadido con éxito!')
            return redirect('lista_user')

    return render(request, 'lista_users.html')

def borrar_user(request, id_Usuario):
    user = Users.objects.get(id_Usuario=id_Usuario)
    user.delete()
    messages.info(request, 'User eliminado')
    return redirect('lista_user')

def edit_user(request, id_Usuario):
    edita_user = Users.objects.get(id_Usuario=id_Usuario)  

    user_lista = Users.objects.all()
    valor = {
        'edita_user': edita_user,
        'user_lista': user_lista
    }
    return render(request, 'lista_users.html', valor)

def edi_user(request, id_Usuario):
    user = Users.objects.get(id_Usuario=id_Usuario)
    if request.method == 'POST':
        user.Username = request.POST['Username']
        user.Contraseña = request.POST['Contraseña']
        user.Email = request.POST['Email']
        user.Dirección = request.POST['Dirección']
       
        user.save()
        messages.success(request, 'User actualizado con éxito')
        
        return redirect('lista_user')

    return redirect('lista_user')
