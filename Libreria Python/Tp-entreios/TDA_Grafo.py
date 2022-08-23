class ciudad():
    def __init__(self, nombre, cp):
        self.nombre = nombre
        self.cp = cp
        self.idCiudad = None
        
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getCP(self):
        return self.cp
    
    def setCP(self, cp):
        self.cp = cp
    
    def setIdCiudad(self, idCiudad):
        self.iidCiudad = idCiudad
        
    def getIdCiudad(self):
        return self.idCiudad
        
        
class viaje():
    def __init__(self, origen, ciudad, importe, distancia):
        self.origen = origen
        self.ciudad = ciudad
        self.importe = importe
        self.distancia = distancia
        self.idViaje = None
        
    def getOrigen(self):
        return self.origen
    
    def setOrigen(self, origen):
        self.origen = origen
        
    def getCiudad(self):
        return self.ciudad
    
    def setCiudad(self, ciudad):
        self.ciudad = ciudad
    
    def getImporte(self):
        return self.importe
    
    def setImporte(self, importe):
        self.importe = importe
        
    def getDistancia(self):
        return self.distancia
    
    def setDistancia(self, distancia):
        self.distancia = distancia
        
    def getIdViaje(self):
        return self.idViaje

    def setIdViaje(self, idViaje):
        self.idViaje = idViaje

class nodoVertice():
    def __init__(self):
        self.ciud = None
        self.cab = None
        self.sig = None
    
    def insertar(self, nodo):
        if((self.cab==None) or (nodo.info.getCiudad().getNombre() < self.cab.info.getCiudad().getNombre())):
            nodo.sig = self.cab
            self.cab = nodo
        else:
            ant = self.cab
            act = self.cab.sig
            while (act != None and (act.info.getCiudad().getNombre() < nodo.info.getCiudad().getNombre())):
                ant=act
                act=act.sig
            nodo.sig=act
            ant.sig=nodo
        
    def buscar(self, busk):
        act = self.cab
        while ((act!=None) and (act.info.getCiudad().getNombre() != busk)):
            act=act.sig
        return act
    
    
class nodoArista():
    def __init__(self):
        self.info = None
        self.sig = None
    
    
class grafo():
    def __init__(self):
        self.cab = None
        
    def insertar(self, nodo):
        if ((self.cab == None) or (nodo.ciud.getNombre() < self.cab.ciud.getNombre())):
            nodo.sig=self.cab
            self.cab=nodo
        else:
            ant=self.cab
            act=self.cab.sig
            while (act != None) and (act.ciud.getNombre() < nodo.ciud.getNombre()):
                ant=act
                act=act.sig
            nodo.sig=act
            ant.sig=nodo
              
    def altaVertice(self, ciudad):
        pos=self.buscar(ciudad.getNombre())
        if pos==None:
            nodo=nodoVertice()
            nodo.cab=None
            nodo.ciud=ciudad
            self.insertar(nodo)
            return True
        else:
            return False
            
    def generarArco(self, viaje):        
        pos = self.buscar(viaje.getOrigen())
        if (pos != None):
            pos2 = self.buscar(viaje.getCiudad().getNombre())
            if (pos2 != None):
                i = pos.buscar(viaje.getCiudad().getNombre())
                if i == None:
                    nodo=nodoArista()
                    nodo.info=viaje
                    pos.insertar(nodo)
                    return True
                else:
                    print("El arco ya esta formado")
                    return False
            else:
                print("No esta la ciudad destino")
                return False
        else:
            print("No se encontro la ciudad origen")
            return False
            
    def buscar(self, busk):
        act = self.cab
        while ((act!=None) and (act.ciud.getNombre() != busk)):
            act=act.sig
        return act
                    
    def listarGrafo(self):
        if (self.cab!= None): 
            act=self.cab
            while act != None:                
                print("Ciudad: "+act.ciud.getNombre() + " ")
                if (act.cab!=None):
                    print("Puede viajar a: ")
                    aux=act.cab
                    while aux != None:
                        print(aux.info.getCiudad().getNombre() + ", distancia: " + str(aux.info.getDistancia()))
                        aux=aux.sig
                    print()
                act=act.sig 
        else: print("grafo vacio")
    
    def tomarCiud(self):
        lista_Ciud =[]
        act=self.cab
        while(act!=None):
            lista_Ciud.append(act.ciudad)
            act = act.sig
        return lista_Ciud
        
    def tomarCam(self):
        if self.cab != None:    
            caminos=[]
            v=self.cab
            while v!=None:
                if v.cab!=None:
                    cam=v.cab
                    while cam != None:
                        caminos.append(v.ciudad+"|"+cam.ciudad)
                        cam=cam.sig
                v=v.sig
            return caminos
        else:
            return None
            
'''            
g=grafo()
rdt = ciudad('Rosario del Tala', 3174)
cdu = ciudad('Concepcion del Uruguay', 3260)
ny = ciudad('Nogoya', 3150)
bs = ciudad('Basavilbaso', 3170)
mc = ciudad('Macia', 3177)
g.altaVertice(rdt)
g.altaVertice(cdu)
g.altaVertice(ny)
g.altaVertice(bs)
g.altaVertice(mc)
viaj = viaje(rdt, bs, 80 ,50)

g.generarArco(viaj)
g.generarArco(viaje(rdt, cdu, 130, 90))
g.generarArco(viaje(mc, ny, 160, 110))
g.listarGrafo()
'''









'''
def insertarEnGrafoV(g,nodo):
    Aux = nodoVertice()
    Aux.id = nodo.id
    Aux.Ciudad = nodo.Ciudad
    Aux.Latitud = nodo.Latitud
    Aux.Longitud = nodo.Longitud
    Aux.Direccion =  nodo.Direccion
    Aux.Telefono = nodo.Telefono
    if ((g.cabecera==None) or (Aux.id<g.cabecera.id)):
        Aux.sig = g.cabecera
        g.cabecera=Aux
    else:
        ant=g.cabecera
        act=g.cabecera.SigVertice
        while ((act!=None) and (act.id<Aux.id)):
            ant=ant.SigVertice
            act=act.SigVertice
        Aux.SigVertice=act
        ant.SigVertice=Aux
    g.tamanio+=1
   
def insertarEnGrafoA(g,nodo):
    Aux = nodoArista()
    Aux.id = nodo.id
    Aux.ciudOr = nodo.ciudOr
    Aux.ciudDest = nodo.ciudDest
    Aux.distancia = nodo.distancia
    Aux.tiempo = nodo.tiempo
    Aux.empresa =  nodo.empresa
    Aux.horaSalida = nodo.horaSalida
    Aux.importe = nodo.importe
    if ((g.cabecera==None) or (Aux.id<g.cabecera.id)):
        Aux.SigArista = g.cabecera
        g.cabecera=Aux
    else:
        ant=g.cabecera
        act=g.cabecera.SigArista
        while ((act!=None) and (act.id<Aux.id)):
            ant=ant.SigArista
            act=act.SigArista
        Aux.SigArista=act
        ant.SigArista=Aux
    g.tamanio+=1

def TotalReg(g):
    return g.tamanio
        
def eliminar(g,buscado):
    if (g.cabecera.ciudad==buscado):
        x=g.cabecera.ciudad
        g.cabecera=g.cabecera.sig
    else:
        ant=g.cabecera
        act=g.cabecera.sig
        while ((act!=None) and (act.ciudad!=buscado)):
            ant=ant.sig
            act=act.sig
        if (act!=None):
            x=act.ciudad
            ant.sig=act.sig
    return x  
    
def eliminarArcos(vertice,buscado):
    aux=vertice
    while (aux!=None):
        eliminar(aux,buscado)
        aux=aux.sig
        
def eliminarDegrafo(g,buscado):
    eliminar(g,buscado) #elimina el vertice
    eliminarArcos(g.cabecera,buscado)

def eliminarRelacion(g,vertice,arista):
    posvertice=buscarEnGrafo(g,vertice)
    if (posvertice!=None):
        eliminar(posvertice,arista)
    
def buscarEnGrafo(g,buscado):
    pos=None
    act=g.cabecera
    while (act!=None) and (act.id!=buscado.id):
        act=act.sig
    if (act==None):
        pos=act
    return pos 

def altaArco(g,vertice,arista):
    posvertice=buscarEnGrafo(g,vertice)
    if (posvertice!=None) and (buscarEnGrafo(g,arista)!=None)and (buscarEnGrafo(posvertice,arista)==None):
        nodo=nodoArista()
        insertarEnGrafoA(posvertice,nodo,arista)
        
def altaVertice(g,vertice):
    if (buscarEnGrafo(g,vertice)==None):
        insertarEnGrafoV(g,vertice)
        
def listar(g):
    act = g.cabecera
    while (act!=None):
        print("\nID: "+str(act.id)+"\nCiudad: "+act.Ciudad+"\nLatitud: "+act.Latitud)
        print("Longitud: "+act.Longitud+"\nDirección: "+act.Direccion+"\nTelefono: "+act.Telefono)
        act = act.sig      
        
def bucle(g,vertice):       #relacion reflexiva 
    posvertice=buscarEnGrafo(g,vertice)
    if ((posvertice!=None) and (buscarEnGrafo(posvertice,vertice)!=None)):
        return True
    else:
        return False

def cargarEtiquetas(g):
    act=g.cabecera
    while (act!=None):
        actArco=act.cabecera
        while(actArco!=None):
            actArco.etiqueta=int (input("Ingrese Etiqueta de ",+act.ciudad+" y "+actArco.ciudad+": "))
            actArco=actArco.sig
        act=act.siguiente     
        
def crearMarca(g): #inicializa en FALSE, no visitado
    marca=[]
    act=g.cabecera
    while (act!=None):
        marca.append(False)
        act=act.sig
    return marca


'''    
"""
def bpp (vertice, marca): #Búsqueda primero en profundidad
marca[v]:= visitado
para cada nodo w adyacente a v hacer
si marca[w] = noVisitado entonces
bpp(w)
"""