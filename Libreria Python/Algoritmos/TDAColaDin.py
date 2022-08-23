class cola():
    fre,fin,tam=None,None,0
 
class nodoQ():
    info,sig=None,None
    
#q=cola()
    
def colaVacia(q):
    return q.fre==None

def colaLlena(q):
    return False
    
def tamañoCola(q):
    return q.tam
    
def insertarEnCola(q,x):
    aux=nodoQ()
    aux.info=x
    aux.sig=None
    if colaVacia(q):
        q.fre = aux
    else:
        q.fin.sig = aux
    q.fin=aux    
    q.tam+=1
    
    
def eliminarDeCola(q):
    x=q.fre.info
    q.fre=q.fre.sig
    if colaVacia(q):
        q.fin=None
    q.tam-=1
    return x