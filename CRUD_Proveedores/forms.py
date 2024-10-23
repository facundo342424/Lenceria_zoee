from django import forms
from .models import Proveedores

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['id_Proveedor', 'Nombre', 'Telefono', 'Correo_electronico','Direccion','Apellido']