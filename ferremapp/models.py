from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class Usuario(AbstractUser):
    is_admin = models.BooleanField('Es Admin', default=False)
    is_vendedor = models.BooleanField('Es Vendedor', default=False)
    is_bodeguero = models.BooleanField('Es Bodeguero', default=False)
    is_contador = models.BooleanField('Es Contador', default=False)
    is_cliente = models.BooleanField('Es Cliente', default=False)

class Producto(models.Model):
    codigo_producto = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=datetime.now)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
