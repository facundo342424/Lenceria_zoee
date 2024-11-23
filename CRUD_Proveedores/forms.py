# forms.py
from django import forms
from .models import Proveedores

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['id_Proveedor', 'Nombre', 'Apellido', 'Telefono','Correo_electronico','Dirección']