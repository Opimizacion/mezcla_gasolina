from django.contrib.auth.models import User, Group
from rest_framework import serializers
from optimizacion.modelos.producto import Producto
from optimizacion.modelos.caracteristica import Caracteristica
from optimizacion.util.data_json import attempt_json_deserialize


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CaracteristicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Caracteristica
        fields = ['nombre', 'valor']
    
   # def to_representation(self, data):
   #   res = super(CaracteristicaSerializer, self).to_representation(data)
   #   return {res['nombre']: res}
        
class ProductoSerializer(serializers.ModelSerializer):
    caracteristicas = CaracteristicaSerializer(read_only=True,many=True)
   
    class Meta:
        model = Producto
        fields = ['pk','nombre','abreviatura','caracteristicas']

    def create(self, validated_data):
        caracteristicas_data = validated_data.pop('caracteristicas')
        producto = Producto.objects.create(**validated_data)
        for data in caracteristicas_data:
            Caracteristica.objects.create(producto=producto, **data)
        return producto

    def update(self, instance, validated_data,*args, **kwargs):
        print(args, kwargs)
        producto = Producto.objects.update(**validated_data)

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.abreviatura = validated_data.get('abreviatura', instance.abreviatura)
       
        request = self.context['request']
        id=request.data.get('pk')
        caracteristicas_data = request.data.get('caracteristicas')
        caracteristicas_data = attempt_json_deserialize(caracteristicas_data, expect_type=list)
        pr = Producto.objects.get(id = id).caracteristicas.all()
        for a in pr:
            a.delete()
       
        caracteristicas_objs = [Caracteristica.objects.create(producto=instance,**data) for data in caracteristicas_data]
        validated_data['caracteristicas'] = caracteristicas_objs
        instance = super().update(instance, validated_data)
        instance.save()
        return instance
   
    