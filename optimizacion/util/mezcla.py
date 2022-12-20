    #Este metodo se usa para calcular las caracteristicas reformadas m3d y tpd
def obtenerReformado (prodCarat1, prodCarat2):
        return prodCarat1 + prodCarat2 

    #Este metodo se usa para calcular las caracteristicas reformadas 
    # Densidad "gravedad especifica" (desidadProd1 * m3dProducto1 + desidadProd2 * m3dProducto2) / m3dReformado
    # Azufre (azufreProd1 * tpdProd1 + azufreProd2 * tpdProd2) / tpdReformado 
    # RBN (rbnProd1 * m3dProd1 + rbnProd2 * m3dProd2) / m3dReformado 
    # IMPVR (IMPVRProd1 * m3dProducto1 + IMPVRProd2 * m3dProducto2) / m3dReformado
    # volumen de nafta (naftaProd1 * m3dProducto1 + naftaProd2 * m3dProducto2) / m3dReformado
    # Arom vol (aromProd1 * m3dProducto1 + aromProd2 * m3dProducto2) / m3dReformado
def sumaPonderada (caratTipo1Prod1, volumenProd1, caratTipo1Prod2, volumenProd2):
        return (caratTipo1Prod1 * volumenProd1 + caratTipo1Prod2 * volumenProd2) / (volumenProd1+volumenProd2)

#Indice lineal RBN to get RON
def obtenerRBNtoROM (rbnReformado):
        a= -1903.4286
        b= 101.70157
        c= -1.9829933
        d= 0.017595832
        e=-0.00005976918
        x= rbnReformado
        return a + b*x +(c * pow(x,2))+ (d * pow(x,3)) + (e * pow(x,4))

#Indice lineal IMPVR to get RVP
def obtenerIMPVtoRVP (IMPVRRef):
        return pow(IMPVRRef,0.82)

def mezcla (productos):
    caratReformada = []
    rbnReformado = sumaPonderada(productos[0]['RBN'], productos[0]['M3d'], productos[1]['RBN'], productos[1]['M3d'])
    IMPVRRef = sumaPonderada(productos[0]['IMPVR'], productos[0]['M3d'], productos[1]['IMPVR'], productos[1]['M3d'])

    caratReformada.append({'nombre': 'm3/d' , 'valor': obtenerReformado(productos[0]['M3d'], productos[1]['M3d'])})  
    caratReformada.append({'nombre': 'TPD' , 'valor': obtenerReformado(productos[0]['TPD'] , productos[1]['TPD'])}) 
    caratReformada.append({'nombre': 'Dens, TON/M3' , 'valor': sumaPonderada(productos[0]['Dens'], productos[0]['M3d'], productos[1]['Dens'], productos[1]['M3d'])})
    caratReformada.append({'nombre': 'RBN' , 'valor': rbnReformado})
    caratReformada.append({'nombre': 'RON' , 'valor': obtenerRBNtoROM(rbnReformado)})  
    caratReformada.append({'nombre': 'IMPVR' , 'valor':IMPVRRef})     
    caratReformada.append({'nombre': 'RVP, atm' , 'valor': obtenerIMPVtoRVP(IMPVRRef)})
    caratReformada.append({'nombre': 'Naft. % Vol' , 'valor':  sumaPonderada(productos[0]['Naft'], productos[0]['M3d'], productos[1]['Naft'], productos[1]['M3d'])}) 
    caratReformada.append({'nombre': 'Arom. %Vol' , 'valor':  sumaPonderada(productos[0]['Arom'], productos[0]['M3d'], productos[1]['Arom'], productos[1]['M3d'])}) 
    caratReformada.append({'nombre': 'Azufre, PPM' , 'valor':  sumaPonderada(productos[0]['Azufre'], productos[0]['TPD'], productos[1]['Azufre'], productos[1]['TPD'])}) 
     
    return caratReformada