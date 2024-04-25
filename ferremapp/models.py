from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuario(AbstractUser):
    is_admin = models.BooleanField('Es Admin', default=False)
    is_vendedor = models.BooleanField('Es Vendedor', default=False)
    is_bodeguero = models.BooleanField('Es Bodeguero', default=False)
    is_contador = models.BooleanField('Es Contador', default=False)
    is_cliente = models.BooleanField('Es Cliente', default=False)