def formatResult (resultado, demanda):
    result={'83': [], '90': [], '94': [], 'Nex': []}
    total = []
    for index in resultado['solucion'][21:]:
        valor= index[1]
        for x in resultado['solucion'][:19]:
            if valor in x:
                result[valor].append({'label':abrebiToName(x[1]),'value':round(x[3],2),'porciento':porciento(x[3],index[2])})
        result[valor].append({'label':'Total','value':round(index[2],2),'porciento':100})
        print(valor)
        demanda[valor]['nombre'] = 'Nafta Exceso' if valor == 'Nex' else 'Gasolina ' + valor
        demanda[valor]['valor'] = round(index[2],2)
        total.append(demanda[valor])
    return result, total
            

def abrebiToName (x):
    if x == 'Nvl':
         return 'Nafta Ligera'
    if x == 'Np':
        return 'Nafta Pesada'
    if x == 'Ref':
        return 'Reformado'
    if x == 'Ncraq':
        return 'Nafta Craqueada Importación'
    if x == 'Ni':
        return 'Nafta Importación'

def porciento (x , y):
    return round((x / y) * 100 ,2)

