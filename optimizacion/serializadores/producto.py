from rest_framework import serializers
from optimizacion.modelos.producto import Producto
from optimizacion.serializadores.caracteristicas import CaracteristicaSerializer
from optimizacion.modelos.caracteristica import Caracteristica
from optimizacion.util.data_json import attempt_json_deserialize

class ProductoSerializer(serializers.ModelSerializer):
    caracteristicas = CaracteristicaSerializer(many=True)
   
    class Meta:
        model = Producto
        fields = ['pk','nombre','abreviatura','caracteristicas']

    def create(self, validated_data):
        caracteristicas_data = validated_data.pop('caracteristicas')
        producto = Producto.objects.create(**validated_data)
        for data in caracteristicas_data:
            Caracteristica.objects.create(producto=producto, **data)
        return producto

    def update(self, instance, validated_data):

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.abreviatura = validated_data.get('abreviatura', instance.abreviatura)
        instance.save()

        items = validated_data.get('caracteristicas')
        caract_db=instance.caracteristicas.all()
        ids=[]
        for item in items:
            item_id = item.get('id', None)
            if item_id:
                ids.append(item_id)
                caract_item = Caracteristica.objects.get(id=item_id, producto=instance)
                caract_item.nombre = item.get('nombre', caract_item.nombre)
                caract_item.valor = item.get('valor', caract_item.valor)
                caract_item.save()
            else:
                c=Caracteristica.objects.create(producto=instance, **item)
                c.save()
                ids.append(c.id)

        for index in caract_db:
            if index.id not in ids:
                index.delete()
        return instance
   
    