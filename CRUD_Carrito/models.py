from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'



class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)



class caja(models.Model):
    id_caja = models.BigAutoField(db_column='id_caja', primary_key=True)
    id_Empleado = models.ForeignKey('empleados', models.DO_NOTHING, db_column='id_Empleado')  # Field name made lowercase.
    id_Factura = models.ForeignKey('facturas', models.DO_NOTHING, db_column='id_Factura')   # Field name made lowercase.
    Fecha_apertura_caja = models.DateTimeField(db_column='Fecha_apertura_caja',default=timezone.now, blank=False, null=False)  # Field name made lowercase.
    Fecha_cierre_caja = models.DateTimeField(db_column='Fecha_cierre_caja', blank=True, null=True)  # Field name made lowercase.
    Monto_inicial_Caja = models.DecimalField(db_column='Monto_inicial_Caja', max_digits=8, decimal_places=2)  # Field name made lowercase.
    Total_ingresos_caja = models.DecimalField(db_column='Total_ingresos_caja', max_digits=8, decimal_places=2, null=True)
    Total_egresos_caja = models.DecimalField(db_column='Total_egresos_caja', max_digits=8, decimal_places=2, null=True)
    numero = models.DecimalField(db_column='numero', max_digits=8, decimal_places=2) 
    created_at = models.DateTimeField(default=timezone.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now,blank=True, null=True)
   

    class Meta:
        managed = True
        db_table = 'caja'




class Clientes(models.Model):
    id_Cliente = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Domicilio = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=15)  # Changed to CharField for phone number
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Clientes'


class users(models.Model):
    id_Usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    Contraseña = models.DecimalField(max_digits=10, decimal_places=2)
    email= models.CharField(max_length=100)
    Direccón = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
            




class facturas(models.Model):
    id_Factura = models.BigAutoField(db_column='id_Factura', primary_key=True)
    id_Venta = models.ForeignKey('ventas', models.DO_NOTHING, db_column='id_Venta')  # Field name made lowercase.
    fecha_emision_factura = models.DateTimeField(db_column='fecha_emision_factura')  # Field name made lowercase.
    monto_total_factura = models.DecimalField(db_column='monto_total_factura', max_digits=8, decimal_places=2)
    metodo_de_pago_factura = models.CharField(db_column='metodo_de_pago_factura', max_length=191)  # Field name made lowercase. # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facturas'



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class empleados(models.Model):
    id_Empleado = models.BigAutoField(db_column='id_Empleado', primary_key=True)  # Field name made lowercase.
    Nombre = models.CharField(db_column='Nombre', max_length=191)  # Field name made lowercase.
    Apellido = models.CharField(db_column='Apellido', max_length=191)  # Field name made lowercase.
    Telefono = models.IntegerField(db_column='Telefono') 
    correo_electronico= models.CharField(db_column='correo_electronico', max_length=191)
    DNI = models.IntegerField(db_column='DNI') # Field name made lowercase.
    Dirección = models.CharField(db_column='Dirección', max_length=191)  # Field name made lowercase.
    Localidad = models.CharField(db_column='Localidad', max_length=191)  # Field name made lowercase. # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'empleados'



class TipodeVenta(models.Model):
    id_TipoVenta = models.BigAutoField(db_column='id_TipoVenta', primary_key=True)
    Nombre_de_tipo_de_venta = models.CharField(db_column='Nombre_de_tipo_de_venta', max_length=191)
    Descripción = models.CharField(db_column='Descripción', max_length=191)
    Fecha_Creación = models.DateTimeField(db_column='Fecha_Creación')  
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TipodeVenta'

class Productos(models.Model):
    id_Producto = models.BigAutoField(db_column='iIdProducto', primary_key=True)  
    Nombre = models.CharField(db_column='Nombre', max_length=191)  # Field name made lowercase.
    Marca = models.CharField(db_column='Marca', max_length=191)  # Field name made lowercase.
    Precio = models.IntegerField(db_column='Precio')  # Field name made lowercase.
    Color = models.IntegerField(db_column='Color')  # Field name made lowercase. # Field name made lowercase.
    surl = models.CharField(db_column='sUrl', max_length=250)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

   
    class Meta:
        managed = False
        db_table = 'Productos'

class Ventas(models.Model):
    id_Venta = models.BigAutoField(db_column='id_Venta', primary_key=True)  # Field name made lowercase.
    id_Empleado = models.ForeignKey(empleados, models.DO_NOTHING, db_column='id_Empleado',null=True)
    id_Cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_Cliente')
    id_TipoVenta = models.ForeignKey(TipodeVenta, models.DO_NOTHING, db_column='id_TipoVenta')
    fecha_venta = models.DateTimeField(db_column='fecha_venta') 
    hora_venta = models.TimeField(db_column='hora_venta', default=timezone.now)  # Field name made lowercase.
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'ventas'

class Stock(models.Model):
    id_stock = models.BigAutoField(db_column='id_stock', primary_key=True)
    id_Producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_Producto')  # Field name made lowercase.
    disponible_stock = models.DecimalField(max_digits=10, decimal_places=2)
    minimo = models.DecimalField(max_digits=10, decimal_places=2)
    maximo = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    list_display = ['id_Producto', 'disponible_stock','minimo','maximo']
    
    class Meta:
        managed = False
        db_table = 'Stock'


class DetalleVenta(models.Model):
    id_detalle_venta = models.BigAutoField(db_column='id_detalle_venta', primary_key=True)  # Field name made lowercase.
    id_Producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_Producto')
    id_Venta = models.ForeignKey(Ventas, models.DO_NOTHING, db_column='id_Venta')
    cantidad_de_productos_detalle_de_ventas= models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario_venta= models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_venta= models.DecimalField(max_digits=10, decimal_places=2) # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalleVenta'









