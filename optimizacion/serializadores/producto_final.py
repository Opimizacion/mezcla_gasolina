from rest_framework import serializers
from optimizacion.modelos.producto_final import ProductoFinal
from optimizacion.modelos.restriccion_producto import RestriccionProducto
from optimizacion.serializadores.restriccion_producto import RestriccionProductoSerializer

class ProductoFinalSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = ProductoFinal
        fields = ['id','nombre', 'precio', 'demandaMin', 'demandaMax']


class ProductoEspecificacionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(required=False)
    restricciones = RestriccionProductoSerializer(many=True)
    class Meta:
        model = ProductoFinal
        fields = ['id','nombre', 'restricciones']        

    def create(self, validated_data):
        restricciones_data = validated_data.pop('restricciones')
        producto = ProductoFinal.objects.create(**validated_data)
        for data in restricciones_data:
            RestriccionProducto.objects.create(producto=producto, **data)
        return producto

    def update(self, instance, validated_data):

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.save()

        items = validated_data.get('restricciones')
        caract_db=instance.restricciones.all()
        ids=[]
        for item in items:
            item_id = item.get('id', None)
            if item_id:
                ids.append(item_id)
                restri_item = RestriccionProducto.objects.get(id=item_id, producto=instance)
                restri_item.nombre = item.get('nombre', restri_item.nombre)
                restri_item.valor = item.get('valor', restri_item.valor)
                restri_item.save()
            else:
                c=RestriccionProducto.objects.create(producto=instance, **item)
                c.save()
                ids.append(c.id)

        for index in caract_db:
            if index.id not in ids:
                index.delete()
        return instance