from django.db import models

class Tienda(models.Model):
  direccion = models.CharField(max_length=32, blank=True, null=True, unique=True)
  provincia = models.CharField(max_length=32, blank=True, null=True)
  region = models.CharField(max_length=32, blank=True, null=True)
  fechaCreacion = models.CharField(max_length=32, blank=True, null=True)
  telefono = models.CharField(max_length=32, blank=True, null=True, unique=True)

class Producto(models.Model):
  descripcion = models.CharField(max_length=32, blank=True, null=True)
  codigo = models.CharField(max_length=32, blank=True, null=True, unique=True)
  precioVenta = models.CharField(max_length=32, blank=True, null=True)
  cantidad = models.CharField(max_length=32, blank=True, null=True)
  tiendaRelacionada = models.ForeignKey(Tienda,on_delete=models.SET_NULL,blank=True, null=True)