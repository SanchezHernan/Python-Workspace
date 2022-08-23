def bBinRec(unaLista, item):
    if len(unaLista) == 0:
        return False
    else:
        puntoMedio = len(unaLista)//2
        if unaLista[puntoMedio]==item:
            return True
        else:
            if item<unaLista[puntoMedio]:
                return bBinRec(unaLista[:puntoMedio],item)
            else:
                return bBinRec(unaLista[puntoMedio+1:],item)

listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(bBinRec(listaPrueba, 3))
print(bBinRec(listaPrueba, 13))