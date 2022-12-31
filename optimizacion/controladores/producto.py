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
from optimizacion.util.estimacion import redimientoReformador
from optimizacion.util.modelo import formatResult
from optimizacion.matematica.optmizacion_mezcla.docplex.mezcla import run
import json

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


    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def detallesResultantes(request, format=None):
        productos = prod_by_ids(request.data['ids'])
        estimacionRef = redimientoReformador(94)

        # Datos y Estructuras
        pInt = {'Nvl', 'Np', 'Ref'}
        pFin = {'83', '90', '94'}
        # productos bd 
        pIntC = {
            'Nvl': {'Rendimiento': 0.04776, 'RBN': productos[0]['RBN'], 'IMPVR': productos[0]['IMPVR'], 'PAzufre': productos[0]['Azufre']*productos[0]['Dens'], 'Densidad': productos[0]['Dens']},
            'Np':  {'Rendimiento': 0.151957, 'RBN': productos[1]['RBN'], 'IMPVR': productos[1]['IMPVR'], 'PAzufre': productos[1]['Azufre']*productos[1]['Dens'], 'Densidad': productos[1]['Dens']},
            'Ref': {'Rendimiento': estimacionRef['C5+']/100, 'RBN': estimacionRef['RBN'], 'IMPVR': estimacionRef['IMPVR'], 'PAzufre': estimacionRef['Azufre']*estimacionRef['Dens'], 'Densidad': estimacionRef['Dens']},
        }
        pFinC = {
            '83': {'price': 3300, 'RBNmin': 58.89, 'IMPVRmax': 0.617498832595756, 'Azufemax': 1000, 'Densidadmin': 0.7200},
            '90': {'price': 3500, 'RBNmin': 62.36, 'IMPVRmax': 0.617498832595756, 'Azufemax': 1000, 'Densidadmin': 0.7200},
            '94': {'price': 3746, 'RBNmin': 65.13, 'IMPVRmax': 0.617498832595756, 'Azufemax': 1000, 'Densidadmin': 0.7200}
        }  
        demandaPF = {
            '83': {'Min': 0, 'Max': 'M'},
            '90': {'Min': 750, 'Max': 'M'},
            '94': {'Min': 300, 'Max': 'M'}
        }
        destil = 8744
        try:
            modelo = run (pInt,pFin,pIntC,pFinC,demandaPF,destil)
            gasolina, totales= formatResult(modelo, demandaPF)
            return Response({'modelo_estado': True,'result': gasolina,'total': totales}, status=status.HTTP_201_CREATED)
        except Exception as inst:
            print(type(inst))    # the exception instance
            print(inst)
            return Response({'modelo_estado': False,'result': inst}, status=status.HTTP_201_CREATED)
            
        
