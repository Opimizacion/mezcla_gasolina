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

    def detallesResultantes(request, format=None):
        # Datos y Estructuras
        pInt = {'Nvl', 'Np', 'Ref'}
        pFin = {'G83', 'G90', 'G94'}
        productos = prod_by_ids(request.data['ids'])
        # productos bd 
        pIntC = {
            'Nvl': {'Rendimiento': 0.04776, 'RBN': productos[0]['RBN'], 'RVP': productos[0]['RVP'], 'PAzufre': productos[0]['Azufre'], 'Densidad': productos[0]['Dens']},
            'Np':  {'Rendimiento': 0.151957, 'RBN': productos[1]['RBN'], 'RVP': productos[1]['RVP'], 'PAzufre': productos[1]['Azufre'], 'Densidad': productos[1]['Dens']},
            'Ref': {'Rendimiento': 0.82455, 'RBN': productos[2]['RBN'], 'RVP': productos[2]['RVP'], 'PAzufre': productos[2]['Azufre'], 'Densidad': productos[2]['Dens']},
        }
        pFinC = {
            'G83': {'price': 3300, 'RBNmin': 58.89, 'RVPmax': 0.617498832595756, 'Azufemax': 1000, 'Densidadmin': 0.7200},
            'G90': {'price': 3500, 'RBNmin': 62.36, 'RVPmax': 0.617498832595756, 'Azufemax': 1000, 'Densidadmin': 0.7200},
            'G94': {'price': 3746, 'RBNmin': 65.13, 'RVPmax': 0.617498832595756, 'Azufemax': 1000, 'Densidadmin': 0.7200}
        }    
        demandaPF = {
            'G83': {'Min': 0, 'Max': 'M'},
            'G90': {'Min': 750, 'Max': 'M'},
            'G94': {'Min': 300, 'Max': 'M'}
        }
        

