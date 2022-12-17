from django.shortcuts import render
from rest_framework import generics , status, permissions
from rest_framework.views import APIView
from optimizacion.serializers import ProductoSerializer
from optimizacion.modelos.producto import Producto
from optimizacion.modelos.caracteristica import Caracteristica
from optimizacion.modelos import util
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer    

class mezclaProducto (APIView):
     @api_view(['POST'])
     @permission_classes([IsAuthenticated])
     def productoReformador(request, format=None):
        caracteristica_prod1 = Caracteristica.objects.filter(producto__id= request.data['ids'][0]).values_list('nombre', 'valor', 'producto').order_by('nombre')
        caracteristica_prod2 = Caracteristica.objects.filter(producto__id= request.data['ids'][1]).values_list('nombre', 'valor', 'producto').order_by('nombre')
        #users_with_reports = Producto.objects.filter(caracteristicas__isnull=False,id__in= ids).values_list('nombre','caracteristicas')
       # users =Producto.objects.all().get(id__in = ids)
       # a = Caracteristica.objects.filter(producto__id__in=ids).query.alias_map['optimizacion_producto']
       # print([e for e in Caracteristica.objects.all().filter(producto_id__in = ids)])
        producto_mecla = mezcla(caracteristica_prod1,caracteristica_prod2)
        data = {
            'nombre': 'Nafta a reformador',
            'abreviatura': 'NR',
            'caracteristicas': producto_mecla
        }
        print(producto_mecla)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     #   print ( caracteristicas )

     def mezcla (caract1, caract2):
       caratReformada = []
       m3dProd1 = 0
       m3dProd2 = 0
       m3dReformado = 0
       IMPVRRef = 0
       for value in caract1:
         for caract in caract2:
            if (value.nombre == caract.nombre) and (caract.nombre == 'm3/d' or caract.nombre == 'TPD'):
                caratReformada.append({'nombre': value.nombre , 'valor': obtenerReformado(value.valor, caract.valor)})  
                if caract.nombre == 'm3/d':
                  m3dReformado = obtenerReformado(value.valor, caract.valor)
                  m3dProd1 = value.valor
                  m3dProd2 = caract.valor      

            if (value.nombre == caract.nombre) and (caract.nombre == 'Dens, TON/M3' or caract.nombre == 'RBN' or caract.nombre == 'IMPVR' or caract.nombre == 'Naft. % Vol' or caract.nombre == 'Arom. %Vol'):
                caratReformada.append({'nombre': caract.nombre , 'valor': obtenerCaractReformada(value. valor,m3dProd1, caract2.valor, m3dProd2, m3dReformado)})           
                if caract.nombre == 'IMPVR':
                  IMPVRRef =  obtenerCaractReformada(value.valor, m3dProd1, caract2.valor, m3dProd2, m3dReformado)

            if value.nombre == 'RON' and caract2.nombre == 'RON':
                caratReformada.append({'nombre': 'RON' , 'valor': obtenerRBNtoROM(m3dReformado)})

            if value.nombre == 'RVP, atm' and caract2.nombre == 'RVP, atm':
                caratReformada.append({'nombre': 'RVP, atm' , 'valor': obtenerIMPVtoRVP(IMPVRRef)})             
      
       return caratReformada


