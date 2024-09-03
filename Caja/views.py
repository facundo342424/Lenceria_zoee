from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')  # Asegúrate de que 'home.html' exista en la carpeta de templates

