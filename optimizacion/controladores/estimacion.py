from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from optimizacion.util.querys import prod_by_abrev
from optimizacion.util.estimacion import na, boxc, c5, obtenerRONtoRBN, rvp, imrvp, azufre, densidad
from rest_framework.response import Response
from rest_framework import status

class Estimacion (APIView):
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def redimientoReformador (self):
        ron = 95
        resultado = []
        producto = prod_by_abrev()
        nfa = na(producto[0]['Naft'], producto[0]['Arom'])
        rn = boxc (ron, nfa)
        rp = rvp (producto[0]['RVP'])

        resultado.append({'RON': ron})  
        resultado.append({'N+2A': nfa})
        resultado.append({'boxc5+':rn})
        resultado.append({'C5+': c5( rn )})
        resultado.append({'RBN': obtenerRONtoRBN( ron )})
        resultado.append({'RVP': rp})
        resultado.append({'IMPVR': imrvp(rp)})
        resultado.append({'Azufre': azufre (producto[0]['Azufre'])})
        resultado.append({'Dens': densidad (producto[0]['Dens'])})

        return Response(resultado, status=status.HTTP_201_CREATED)

