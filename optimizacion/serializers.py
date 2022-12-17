from django.contrib.auth.models import User, Group
from rest_framework import serializers
from optimizacion.modelos.producto import Producto
from optimizacion.modelos.caracteristica import Caracteristica


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
    caracteristicas = CaracteristicaSerializer(many=True)

    class Meta:
        model = Producto
        fields = ['pk','nombre', 'abreviatura', 'tipo', 'caracteristicas']

    def create(self, validated_data):
        caracteristicas_data = validated_data.pop('caracteristicas')
        producto = Producto.objects.create(**validated_data)
        for data in caracteristicas_data:
            Caracteristica.objects.create(producto=producto, **data)
        return producto
    