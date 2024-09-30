# forms.py
from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['id_Producto', 'Nombre', 'Marca', 'Precio','Color']
