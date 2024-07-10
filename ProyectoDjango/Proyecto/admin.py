from django.contrib import admin
from .models import Genero, Usuario, Cargo, Categoria, Producto

# Register your models here.
admin.site.register(Genero)
admin.site.register(Cargo)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Producto)
