from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from . forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def register(request):
    data = { 
        'form': CustomUserCreationForm()
        }
    
    if request.method == 'POST':
        user_Creation_form = CustomUserCreationForm(data=request.POST)

        if user_Creation_form.is_valid():
            user_Creation_form.save()

            user = authenticate(username=user_Creation_form.cleaned_data['username'], password=user_Creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('perfil')
        
    return render (request,'registration/register.html',data)

@login_required
def productos(request):
    return render(request, 'productos.html')

def salir(request):
    logout(request)
    return redirect('inicio')

def perfil(request):
    return render(request, 'perfil.html')

