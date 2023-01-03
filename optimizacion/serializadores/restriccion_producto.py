from rest_framework import serializers
from optimizacion.modelos.restriccion_producto import RestriccionProducto
from optimizacion.serializadores.producto_final import ProductoFinalSerializer
from optimizacion.modelos.producto_final import ProductoFinal

class RestriccionProductoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = RestriccionProducto
        fields = ['id','nombre', 'valor', 'producto']