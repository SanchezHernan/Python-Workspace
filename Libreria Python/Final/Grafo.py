class grafo():
    def __init__(self):
        self.cab = None

class nodoVertice():
    def __init__(self):
        self.ciudad = None
        self.cab = None
        self.sig = None
    
class nodoArista():
    def __init__(self):
        self.destino = None
        self.importe = None
        self.distancia = None
        self.sig = None
    
def grafoVacio(g):
    return g.cab == None
    
def insertar(g, x, tipoNodo, dist, imp):
    if tipoNodo == 0:
        aux=nodoVertice()
        aux.cab=None
    else:
        aux=nodoArista()
        aux.distancia = dist
        aux.importe = imp
    aux.ciudad=x
    if ((g.cab == None) or (x<=g.cab.ciudad)):
        aux.sig=g.cab
        g.cab=aux
    else:
        ant=g.cab
        act=g.cab.sig
        while (act != None) and (act.ciudad < x):
            ant=act
            act=act.sig
        aux.sig=act
        ant.sig=aux
    
def altaVertice(g,vert):
    pos=buscar(g,vert)
    if pos==None:
        insertar(g,vert,0,0,0)
    else:
        print("ya existe")
        
def generarArco(g,vert1,vert2, d, imp):
    pos=buscar(g,vert1)
    if (pos != None):
        pos2=buscar(g,vert2)
        if (pos2 != None):
            i=buscar(pos,vert2)
            if i==None:
                insertar(pos,vert2,1,d,imp)
                return True
            else:
                print("El arco ya esta formado")
                return False
        else:
            print("No esta la ciudad origen")
            return False
    else:
        print("No se encontro la ciudad destino")
        return False
        
def buscar(g, busk):
    act = g.cab
    while ((act!=None) and (act.ciudad!=busk)):
        act=act.sig
    return act
        
def listarGrafo(g):
    if (g.cab!= None):    
        act=g.cab
        print("Ciudad: "+act.ciudad + " ")
        if (act.cab!=None):
            print("Puede viajar a: ")
            aux=act.cab
            while aux != None:
                print(aux.ciudad + ", distancia: " + str(aux.distancia))
                aux=aux.sig
            print()
        act=act.sig
        while act!=None:
            print("Ciudad: "+act.ciudad + " ")
            if (act.cab!=None):
                print("puede viajar a: ")
                aux=act.cab
                while aux != None:
                    print(aux.ciudad+ ', distancia: '+ str(aux.distancia))
                    aux=aux.sig
                print()
            act=act.sig    
    else: print("grafo vacio")
    
