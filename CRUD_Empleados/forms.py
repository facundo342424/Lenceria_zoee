from django import forms
from .models import empleados

class CRUD_EmpleadosForm(forms.ModelForm):
    class Meta:
        model = empleados
        fields = ['id_Empleado', 'Nombre', 'Apellido', 'Telefono','correo_electronico','DNI','Dirección','Localidad']
       