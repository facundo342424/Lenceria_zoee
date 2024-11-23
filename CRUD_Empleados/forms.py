# forms.py
from django import forms
from .models import Empleados

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = [ 'Nombre', 'Apellido', 'Telefono','Correo','Dni','Dirección','Localidad']
       