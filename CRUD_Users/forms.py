from django import forms
from models import Users

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['id_Usuario','Username', 'Contraseña', 'Email', 'Dirección']
    