from rest_framework.views import APIView
from rest_framework import generics , status, permissions
from optimizacion.serializadores.producto_final import ProductoFinalSerializer, ProductoEspecificacionSerializer
from optimizacion.modelos.producto_final import ProductoFinal

class ProductoFinalList(generics.ListCreateAPIView):
    queryset = ProductoFinal.objects.all()
    serializer_class = ProductoFinalSerializer

class ProductoFinalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductoFinal.objects.all()
    serializer_class = ProductoFinalSerializer 

class ProductoEspecificacionList(generics.ListCreateAPIView):
    queryset = ProductoFinal.objects.all()
    serializer_class = ProductoEspecificacionSerializer

class ProductoEspecificacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductoFinal.objects.all()
    serializer_class = ProductoEspecificacionSerializer     