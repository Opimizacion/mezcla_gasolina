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
from optimizacion.util.querys import *
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
        demandas = prod_demanda()

        # Datos y Estructuras
        pInt = {'Nvl', 'Np', 'Ref', 'Ni', 'Ncraq'}
        pFin = {'83', '90', '94', 'Nex'}
        # productos bd 
        pIntC = {
            'Nvl': {'Rendimiento': 0.04776, 'RBN': productos[0]['RBN'], 'IMPVR': productos[0]['IMPVR'], 'PAzufre': productos[0]['Azufre']*productos[0]['Dens'], 'Densidad': productos[0]['Dens']},
            'Np':  {'Rendimiento': 0.151957, 'RBN': productos[1]['RBN'], 'IMPVR': productos[1]['IMPVR'], 'PAzufre': productos[1]['Azufre']*productos[1]['Dens'], 'Densidad': productos[1]['Dens']},
            'Ref': {'Rendimiento': estimacionRef['C5+']/100, 'RBN': estimacionRef['RBN'], 'IMPVR': estimacionRef['IMPVR'], 'PAzufre': estimacionRef['Azufre']*estimacionRef['Dens'], 'Densidad': estimacionRef['Dens']},
            'Ni': {'Rendimiento': 0, 'RBN': 0, 'IMPVR': 0, 'PAzufre': 0, 'Densidad': 0},
            'Ncraq': {'Rendimiento': 0, 'RBN': 0, 'IMPVR': 0, 'PAzufre': 0, 'Densidad': 0}
        }
        pFinC = {
            '83': {'price': demandas[0]['precio'], 'RBNmin': demandas[0]['RBNmin'], 'IMPVRmax': demandas[0]['IMPVRmax'], 'Azufemax': demandas[0]['Azufemax'], 'Densidadmin': demandas[0]['Densidadmin']},
            '90': {'price': demandas[1]['precio'], 'RBNmin': demandas[1]['RBNmin'], 'IMPVRmax': demandas[1]['IMPVRmax'], 'Azufemax': demandas[1]['Azufemax'], 'Densidadmin': demandas[1]['Densidadmin']},
            '94': {'price': demandas[2]['precio'], 'RBNmin': round(demandas[2]['RBNmin'],2), 'IMPVRmax': demandas[2]['IMPVRmax'], 'Azufemax': demandas[2]['Azufemax'], 'Densidadmin': demandas[2]['Densidadmin']},
            'Nex': {'price': demandas[3]['precio']}
        }
        demandaPF = {
            '83': {'Min': demandas[0]['demandaMin'], 'Max': 'M' if demandas[0]['demandaMax'] == 0 else demandas[0]['demandaMax']},
            '90': {'Min': demandas[1]['demandaMin'], 'Max': 'M' if demandas[1]['demandaMax'] == 0 else demandas[1]['demandaMax']},
            '94': {'Min': demandas[2]['demandaMin'], 'Max': 'M' if demandas[2]['demandaMax'] == 0 else demandas[2]['demandaMax']},
            'Nex': {'Min': demandas[3]['demandaMin'], 'Max': 'M' if demandas[3]['demandaMax'] == 0 else demandas[3]['demandaMax']}
        }
        destil = 8744
        try:
            modelo = run (pInt,pFin,pIntC,pFinC,demandaPF,destil)
            gasolina, totales= formatResult(modelo, demandaPF)
            return Response({'modelo_estado': True,'result': gasolina,'total': totales}, status=status.HTTP_201_CREATED)
        except Exception as inst:
            print(type(inst))    # the exception instance
            print(inst)
            return Response({'modelo_estado': False,'result': '!! Error al resolver el modelo'}, status=status.HTTP_201_CREATED)
            
        
