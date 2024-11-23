from django.db import models

# Create your models here.
class Users(models.Model):
    id_Usuario = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=100)
    Contraseña = models.CharField(max_length=100) 
    Email = models.CharField(max_length=100)
    Dirección =models.CharField(max_length=100)
    
    class Meta:
        db_table = 'users'
