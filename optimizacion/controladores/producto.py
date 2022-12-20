from django.shortcuts import render
from rest_framework import generics , status, permissions
from rest_framework.views import APIView
from optimizacion.serializers import ProductoSerializer
from optimizacion.modelos.producto import Producto
from optimizacion.modelos.caracteristica import Caracteristica
from optimizacion.util.mezcla import mezcla
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from optimizacion.util.querys import prod_by_ids

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer    

class MezclaProducto (APIView):

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def productoReformador(request, format=None):
        productos = prod_by_ids(request.data['ids'])
        producto_mezcla = mezcla(productos)
        data = {
            'nombre': 'Nafta a reformador',
            'abreviatura': 'NR',
            'caracteristicas': producto_mezcla
        }
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

