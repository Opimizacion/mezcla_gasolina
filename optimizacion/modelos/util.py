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
def obtenerCaractReformada (caratTipo1Prod1, caratTipo1Prod2, caratTipo2Prod1, caratTipo2Prod2, caratTipo2Reformado):
        return (caratTipo1Prod1 * caratTipo2Prod1 + caratTipo1Prod2 * caratTipo2Prod2) / caratTipo2Reformado 
    #Indice lineal RBN to get RON
def obtenerRBNtoROM (rbnReformado):
        return -1903.4286 + 101.70157 * rbnReformado -1.982993 * pow(rbnReformado,2)+ 0.017595832 * pow(rbnReformado,3) -0.00005976918 * pow(rbnReformado,4)
    #Indice lineal IMPVR to get RVP
def obtenerIMPVtoRVP (IMPVRRef):
        return pow(IMPVRRef,0.82)