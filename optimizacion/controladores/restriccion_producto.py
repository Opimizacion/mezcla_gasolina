from rest_framework.views import APIView
from rest_framework import generics , status, permissions
from optimizacion.serializadores.restriccion_producto import RestriccionProductoSerializer
from optimizacion.modelos.restriccion_producto import RestriccionProducto

class RestriccionList(generics.ListCreateAPIView):
    queryset = RestriccionProducto.objects.all()
    serializer_class = RestriccionProductoSerializer

class RestriccionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestriccionProducto.objects.all()
    serializer_class = RestriccionProductoSerializer 