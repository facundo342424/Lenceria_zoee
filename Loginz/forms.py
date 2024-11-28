from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('usuario', 'Usuario Común'),
        ('administrador', 'Administrador'),
        ('superusuario', 'Superusuario'),
    ]

    rol = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'rol']

    def save(self, commit=True):
        user = super().save(commit=False)
        rol = self.cleaned_data['rol']

        if rol == 'administrador':
            user.is_staff = True
        elif rol == 'superusuario':
            user.is_superuser = True
            user.is_staff = True

        if commit:
            user.save()

        return user
