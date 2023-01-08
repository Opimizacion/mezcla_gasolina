from rest_framework import serializers
from optimizacion.modelos.restriccion_producto import RestriccionProducto
from optimizacion.modelos.producto_final import ProductoFinal

class RestriccionProductoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    nombre_producto = serializers.SerializerMethodField()

    class Meta:
        model = RestriccionProducto
        #fields = ['id','nombre', 'valor', 'producto ']
        fields = '__all__'

    def get_nombre_producto (self, obj):
        return obj.producto.nombre