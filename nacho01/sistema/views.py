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
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            # Autenticación y login del usuario
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            
            # Redirección según el tipo de usuario
            if user.is_superuser:
                return redirect('superuser_dashboard')  # Redirigir al panel del superusuario
            elif user.is_staff:
                return redirect('admin_dashboard')  # Redirigir al panel de administrador
            else:
                return redirect('perfil.html')  # Redirigir a la página de usuario normal
        
    return render(request, 'registration/register.html', data)

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            # Autenticación y login del usuario
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            
            # Redirección según el tipo de usuario
            if user.is_superuser:
                return redirect('superuser_dashboard')  # Redirigir al panel del superusuario
            elif user.is_staff:
                return redirect('admin_dashboard')  # Redirigir al panel de administrador
            else:
                return redirect('perfil')  # Redirigir a la página de usuario normal
        else:
            # Si el formulario no es válido, mostrar los errores
            return render(request, 'registration/register.html', {'form': user_creation_form})

    return render(request, 'registration/register.html', data)

@login_required
def productos(request):
    return render(request, 'productos.html')

def salir(request):
    logout(request)
    return redirect('inicio')

@login_required
def perfil(request):
    if request.user.is_superuser:
        return redirect('superuser_dashboard')  # Redirige al panel del superusuario
    elif request.user.is_staff:
        return redirect('admin_dashboard')  # Redirige al panel de administrador
    else:
        return render(request, 'perfil.html')  # Vista de perfil para usuario normal

@login_required
def superuser_dashboard(request):
    if not request.user.is_superuser:
        return redirect('inicio')  # Redirige a inicio si no es superusuario
    return render(request, 'superuser_dashboard.html')  # Vista para superusuario

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('inicio')  # Redirige a inicio si no es administrador
    return render(request, 'admin_dashboard.html')  # Vista para administrador

@login_required
def superuser_dashboard(request):
    if not request.user.is_superuser:
        return redirect('inicio')  # Redirige a inicio si no es superusuario
    return render(request, 'superuser_dashboard.html')  # Vista para superusuario

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('inicio')  # Redirige a inicio si no es administrador
    return render(request, 'admin_dashboard.html')  # Vista para administrador

# views.py
from django.shortcuts import render

def stats_dashboard(request):
    # Tu lógica de la vista para el dashboard de estadísticas
    return render(request, 'stats_dashboard.html')  # Asegúrate de que la plantilla 'stats_dashboard.html' exista



