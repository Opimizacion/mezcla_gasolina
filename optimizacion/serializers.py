from django.contrib.auth.models import User, Group
from rest_framework import serializers
from optimizacion.serializadores.producto import ProductoSerializer
from optimizacion.serializadores.producto_final import ProductoFinalSerializer
from optimizacion.serializadores.restriccion_producto import RestriccionProductoSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

        
