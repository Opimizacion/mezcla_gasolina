from optimizacion.util.querys import prod_by_abrev

# nafta + 2* arom
def na (nafta ,arom):
    return nafta + ( 2 * arom )

def boxc (ron, na):
    return 85.9485 + ( 0.230559 * na ) + ( -0.749819 * ron )

def c5 (boxc):
    x = 21114.8614
    y = 0.33333333
    z = ( boxc - 1 ) * x + 1
    return pow( z, y )

def obtenerRONtoRBN (ron):
        a= 285.24097
        b= -13.216411
        c= 0.27474217
        d= -0.00250797
        e= 0.00000868
        x= ron
        return a + b*x +(c * pow(x,2)) + (d * pow(x,3)) + (e * pow(x,4))

def rvp (rvp):
    print (rvp , pow( rvp, 0.9 ))
    return pow( rvp, 0.9 )

def imrvp (rvp):
    return pow( rvp, 1.25)

def azufre (azufre):
    a = 1.00072
    b = -0.0000244344
    c = 0.000000123264
    d = -0.00000000018195
    return azufre * (1 - (a + b * azufre + (c * pow( azufre, 2)) + (d * pow(azufre, 3))))

def densidad (dens):
    return dens * 1.05    

#ron = 95
 def redimientoReformador (ron):
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

        return resultado    