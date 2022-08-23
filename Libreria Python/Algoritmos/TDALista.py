class lista():
    cab,tam = None, 0
class nodoL():
    info,sig=None,None
    
def listaVacia(l):
    return l.cab==None

def tamañoLista(l):
    return l.tam
       

def insertarEnLista(l,x):
    aux=nodoL()
    aux.info=x
    if ((listaVacia(l)) or (x<l.cab.info)):
        aux.sig=l.cab
        l.cab=aux
    else:
        ant = l.cab
        act = l.cab.sig
        while ((act != None) and (act.info < x)):
            ant=act
            act=act.sig 
        aux.sig=act
        ant.sig=aux
    l.tam+=1
    
def insertarPorNombre(l,x):
    aux=nodoL()
    aux.info=x
    if ((listaVacia(l)) or (x.nom<l.cab.info.nom)):
        aux.sig=l.cab
        l.cab=aux
    else:
        ant = l.cab
        act = l.cab.sig
        while ((act != None) and (act.info.nom < x.nom)):
            ant=act
            act=act.sig 
        aux.sig=act
        ant.sig=aux
    l.tam+=1
    
    
def eliminarDeLista(l,busk):
    x=None
    if l.cab.info == busk:
        x=l.cab.info
        l.cab=l.cab.sig
    else:
        ant=l.cab
        act=l.cab.sig
        while act != None and act.info != busk:
            ant=act
            act=act.sig
        if act != None:
            x=act.info
            ant.sig=act.sig
    l.tam-=1
    return x
    
def insertarDetras(l,busk,x):
    aux=nodoL()
    aux.info=x
    if (listaVacia(l) or l.cab.info == busk):
        aux.sig=l.cab
        l.cab=aux
    else:
        ant = l.cab
        act = l.cab.sig
        while (act.info != busk) and (act != None):
            ant=act
            act=act.sig
        aux.sig=act
        ant.sig=aux
    l.tam+=1
    
def insertarDelante(l,busk,x):
    aux=nodoL()
    aux.info=x
    if listaVacia(l):
        aux.sig=l.cab
        l.cab=aux
    else:
        ant = l.cab
        act = l.cab.sig
        while (ant.info != busk) and (act != None):
            ant=act
            act=act.sig
        aux.sig=act
        ant.sig=aux
    l.tam+=1
    
def mostrarLista(l):
    act=l.cab
    while act != None:
        print(act.info)
        act=act.sig
    
def listarNombres(l):
    act=l.cab
    while act!= None:
        print(act.info.nom)
        act=act.sig
    
#2
def contarNodos(l):
    cont = 0
    if not listaVacia(l):
        act=l.cab
        while act != None:
            act=act.sig
            cont+=1
    return cont

#3
def borrarVocales(l):
    
    while ((not listaVacia(l)) and (l.cab.info in  ("a", "e", "i", "o", "u"))):
        l.cab=l.cab.sig
        l.tam-=1
    if not listaVacia(l):
        ant=l.cab
        act=l.cab.sig
        while act != None:
            if act.info in ("a", "e", "i", "o", "u"):
                ant.sig=act.sig
                l.tam-=1
            ant=act
            act=act.sig
    
#4
def separarEnteros(l):
    li=lista()
    act=l.cab
    while act != None:
        if (act.info%2)==1:
            insertarEnLista(li,eliminarDeLista(l, act.info))
        act=act.sig
    return li        
    
#5
def modificarInfo(l,busk,new):
    act=l.cab
    while act.info != busk:
        act=act.sig
    act.info=new
        
#7
def listarSuma(l):
    act=l.cab
    ac=0
    while act!= None:
        print(act.info)
        ac+=act.info
        act=act.sig
    print("Suma: ",ac)
        
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
    
