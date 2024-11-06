from django.db import models



class Generos(models.Model):
    genero_id = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'generos'    
    
    
class Usuarios(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    fk_genero = models.ForeignKey(Generos, on_delete=models.CASCADE,default=0)
    
    class Meta:
        db_table = 'usuarios'
        
class Productos(models.Model):
    producto_id = models.AutoField(primary_key=True)
    image_producto = models.URLField(max_length=255)
    producto = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'productos'
        
class Cupones(models.Model):
    cupon_id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'cupones'

class Compra(models.Model):
    compra_id = models.AutoField(primary_key=True)
    fk_productos = models.ForeignKey(Productos, on_delete=models.CASCADE)
    fk_usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'compra'
        
class Facturacion(models.Model):
    facturacion_id = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255, blank=True, null=True)
    calle = models.CharField(max_length=255)
    apartamento = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255)
    cp = models.CharField(max_length=255)
    correo = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=255)
    nota = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'facturacion'

class Categorias(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'categorias'
        
class Carrito(models.Model):
    carrito_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'carrito'

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    class Meta:
        db_table = 'carrito_items'
        
class Envio(models.Model):
    envio_id = models.AutoField(primary_key=True)
    compra = models.OneToOneField(Compra, on_delete=models.CASCADE)
    direccion_envio = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=10)
    metodo_envio = models.CharField(max_length=255)
    estado_envio = models.CharField(max_length=255)  
    fecha_envio = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'envios'
        
class Pagos(models.Model):
    pago_id = models.AutoField(primary_key=True)
    compra = models.OneToOneField(Compra, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=255) 
    estado_pago = models.CharField(max_length=255) 
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'pagos'
        
        
class Resenas(models.Model):
    resena_id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    calificacion = models.IntegerField()  # Por ejemplo, entre 1 y 5
    comentario = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'resenas'