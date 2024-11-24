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
                return redirect('user_dashboard')  # Redirigir a la página de usuario normal
        
    return render(request, 'registration/register.html', data)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            
            # Redirigir según el tipo de usuario
            if user.is_superuser:
                return redirect('superuser_dashboard')  # Redirige al dashboard del superusuario
            elif user.is_staff:
                return redirect('admin_dashboard')  # Redirige al dashboard del administrador
            else:
                return redirect('user_dashboard')  # Redirige al dashboard del usuario regular
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})

    return render(request, 'login.html')


@login_required
def productos(request):
    return render(request, 'productos.html')

def salir(request):
    logout(request)
    return redirect('inicio')
@login_required
def productos_Admn(request):
    return redirect(request,'productos.html')

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

def Gestion_Admin(request):
    return render(request, 'Gestion_Admin.html')

def estadistica(request):
    return render(request, 'estadistica.html')



