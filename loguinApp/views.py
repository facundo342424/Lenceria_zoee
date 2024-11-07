from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm, CustomUserCreationForm  # Asegúrate de importar tu formulario personalizado
from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import AuthenticationForm

class CustomLoginView(LoginView):
    login_form = CustomLoginForm  # Utiliza tu formulario personalizado
    login_template = 'registration/login.html'  # Ruta a tu plantilla de inicio de sesión

def home(request):
    return render(request,'home.html')
def lista(request):
    return render(request,'lista.html')

def register(request):
   data = {
        'form': CustomUserCreationForm()
    }
    #validar los campos que vienen del form de register
   if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()

            #usuario que se registra quede logueado, capturo los valores del form
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('Home')
        else:
            data['form'] = user_creation_form
            
   return render(request,'registration/register.html', data)
# Create your views here.
