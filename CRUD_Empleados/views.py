from django.shortcuts import render

def hola(request):
    return render(request,"index.html")

# Create your views here.
