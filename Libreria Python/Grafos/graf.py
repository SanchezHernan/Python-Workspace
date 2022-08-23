class nodoVertice():
    def __init__(self):
        self.info = None
        self.cab = None
        self.sig = None
        
    def insertar(self, nodo):
        if((self.cab==None) or (nodo.info < self.cab.info)):
            nodo.sig = self.cab
            self.cab = nodo
        else:
            ant = self.cab
            act = self.cab.sig
            while (act != None and (act.info < nodo.info)):
                ant=act
                act=act.sig
            nodo.sig=act
            ant.sig=nodo
    '''    
    def buscar(self, busk):
        act = self.cab
        while(act != None and act.info != busk):
            act = act.sig
        return act   
    '''    
class nodoArista():
    def __init__(self):
        self.info = None
        self.sig = None
        
class grafo():
    def __init__(self):
        self.cab = None
        
    def grafoVacio(self):
        return self.cab == None
        
    def insertar(self, nodo):
        if((self.cab==None) or (nodo.info < self.cab.info)):
            nodo.sig = self.cab
            self.cab = nodo
        else:
            ant = self.cab
            act = self.cab.sig
            while (act != None and (act.info < nodo.info)):
                ant=act
                act=act.sig
            nodo.sig=act
            ant.sig=nodo
            
        
    def altaVertice(self, vert):
        pos = self.buscar(vert)
        if pos==None:
            nodo = nodoVertice()
            nodo.cab = None
            nodo.info = vert
            self.insertar(nodo)
        else:
            print('ya existe')
    
    def generarArco(self, vert1, vert2):
        pos = self.buscar(vert1)
        if (pos != None):
            pos2 = self.buscar(vert2)
            if (pos2 != None):
                i = pos.buscar(vert2)
                if i == None:
                    nodo = nodoArista()
                    nodo.info = vert2
                    nodo.sig = None
                    pos.insertar(nodo)
                else:
                    print('El arco ya esta formado')
            else:
                print('No esta el vertice destino')
        else:
            print('No se encontro en vertice de salida')
            
    
    def buscar(self, busk):
        act = self.cab
        while(act != None and act.info != busk):
            act = act.sig
        return act    
        
    def listarGrafo(self):
        if self.cab != None:
            act = self.cab
            while act!= None:
                print('vertice: ' + act.info + ' ')
                if act.cab != None:
                    print('tiene arco con: ')
                    aux=act.cab
                    while aux != None:
                        print(aux.info)
                        aux=aux.sig
                act=act.sig
        else:
            print('grafo vacio')
        

            
           