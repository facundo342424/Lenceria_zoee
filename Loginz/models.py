from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    edad = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField()
    ultimo_login = models.DateTimeField(auto_now=True)
    esta_activa = models.BooleanField(default=True)
    es_personal = models.BooleanField(default=False)
    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')
    class Meta:
        db_table = 'usuario'

