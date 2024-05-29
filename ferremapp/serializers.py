from rest_framework import serializers
from.models import Producto

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['codigo_producto', 'marca', 'codigo', 'nombre', 'fecha', 'valor']