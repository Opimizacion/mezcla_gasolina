from rest_framework import serializers
from optimizacion.modelos.producto_final import ProductoFinal

class ProductoFinalSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = ProductoFinal
        fields = ['id','nombre', 'precio', 'demandaMin', 'demandaMax']