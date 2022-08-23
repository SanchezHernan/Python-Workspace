from Archivos import regArchivo
class lista():
    def __init__(self):
        self.cab=None
        self.tam=0
    
    def eliminarCabecera(self):
        if self.cab!=None:
            x=regArchivo()
            x.info=self.cab.info
            x.pos=self.cab.pos
            self.cab=self.cab.sig
            return x
        else:
            return None
    
class regLista():
    def __init__(self):
        self.pos = None
        self.info = None
    
class nodoL():
    info,pos,sig=None,None,None
    
def listaVacia(l):
    return l.cab==None

def lenght(l):
    return l.tam
       

def insertarEnLista(l,x):
    aux=nodoL()
    aux.info=x.info
    aux.pos=x.pos
    if ((listaVacia(l)) or (x.info<l.cab.info)):
        aux.sig=l.cab
        l.cab=aux
    else:
        ant = l.cab
        act = l.cab.sig
        while ((act != None) and (act.info < x.info)):
            ant=act
            act=act.sig 
        aux.sig=act
        ant.sig=aux
    l.tam+=1
    
def eliminarDeLista(l,busk):
    x=regArchivo()
    if l.cab.info == busk:
        x=l.eliminarCabecera()
    else:
        ant=l.cab
        act=l.cab.sig
        while act != None and act.info != busk:
            ant=act
            act=act.sig
        if act != None:
            x.info=act.info
            x.pos=act.pos
            ant.sig=act.sig
    l.tam-=1
    return x
    

def mostrarLista(l):
    act=l.cab
    while act != None:
        print(act.info)
        act=act.sig
    

def contarNodos(l):
    cont = 0
    if not listaVacia(l):
        act=l.cab
        while act != None:
            act=act.sig
            cont+=1
    return cont

#5
def modificarInfo(l,busk,new):
    act=l.cab
    while act.info != busk:
        act=act.sig
    act.info=new
        
        
def intercepcion(l1,l2):
    act=l2.cab
    l3=lista()
    while not listaVacia(l1):
        x=eliminarDeLista(l1,l1.cab)
        while act != None and x!=act.info:
            act=act.sig
        if act != None:
            insertarEnLista(l3,x)
    return l3
                
def concatenarListas(l1,l2):
    x=eliminarDeLista(l1,l1.cab)
    insertarEnLista(l2,x)
    
def liberarLista(l):
    while not listaVacia(l):
        eliminarDeLista(l,l.cab)
    
