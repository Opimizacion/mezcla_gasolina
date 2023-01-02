from rest_framework import serializers
from optimizacion.modelos.caracteristica import Caracteristica

class CaracteristicaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Caracteristica
        fields = ['id','nombre', 'valor']
