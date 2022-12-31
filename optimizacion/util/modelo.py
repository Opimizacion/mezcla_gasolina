def formatResult (resultado, demanda):
    result={'83': [], '90': [], '94': []}
    total = []
    for index in resultado['solucion'][10:]:
        valor= index[1]
        for x in resultado['solucion'][:9]:
            if valor in x:
                result[valor].append({'label':abrebiToName(x[1]),'value':round(x[3],2),'porciento':porciento(x[3],index[2])})
        result[valor].append({'label':'Total','value':round(index[2],2),'porciento':100})
        demanda[valor]['nombre'] = 'Gasolina ' + valor
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

def porciento (x , y):
    return round((x / y) * 100 ,2)

