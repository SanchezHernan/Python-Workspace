class pila():
    tope, tam= None, 0
    
class nodoP():
    info, sig, ant = None, None, None
    
def pilaLlena(p):
    return False;
    
def pilaVacia(p):
    return p.tope == None
    
def tamañoPila(p):
    return p.tam
    
def apilar(p,x):
    aux = nodoP()
    aux.info = x
    aux.sig = None
    if pilaVacia(p):
        aux.ant = None
    else:
        aux.ant = p.tope
        p.tope.sig = aux
    p.tope = aux
    p.tam+=1
    
def desapilar(p):
    x = p.tope.info
    p.tope = p.tope.ant
    p.tam-=1
    return x
    