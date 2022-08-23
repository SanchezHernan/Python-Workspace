# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 14:42:56 2018

@author: Hornyt0x
"""

class ciudad():
    def __init__(self, nombre, latitud = None, longitud = None):
        self.nombre = nombre
        self.idCiudad = None
        self.latitud = latitud
        self.longitud = longitud
        
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
   
    def setIdCiudad(self, idCiudad):
        self.iidCiudad = idCiudad
        
    def getIdCiudad(self):
        return self.idCiudad
        
    def getLatitud(self):
        return self.latitud
    
    def setLatitud(self, latitud):
        self.latitud = latitud
    
    def getLongitud(self):
        return self.longitud
        
    def setLongitud(self, longitud):
        self.longitud = longitud
        
        
class viaje():
    def __init__(self, origen=None, destino=None, importe=None, distancia=None):
        self.origen = origen
        self.destino = destino
        self.importe = importe
        self.distancia = distancia
        self.idViaje = None
        
    def getOrigen(self):
        return self.origen
    
    def setOrigen(self, origen):
        self.origen = origen
        
    def getDestino(self):
        return self.destino
    
    def setDestino(self, destino):
        self.destino = destino
    
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
        else:
            print("ya existe")
            
    def generarArco(self, viaje):        
        pos = self.buscar(viaje.getOrigen().getNombre())
        if (pos != None):
            pos2 = self.buscar(viaje.getDestino().getNombre())
            if (pos2 != None):
                i = pos.buscar(viaje.getDestino().getNombre())
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
    
    
    def getCiudades(self):
        listaCiud =[]
        act=self.cab
        while(act!=None):
            listaCiud.append(act.ciud)
            act = act.sig
        return listaCiud
        
    def getViajes(self):
        if self.cab != None:    
            viajes=[]
            act=self.cab
            while act!=None:
                if act.cab!=None:
                    viaje=act.cab
                    while viaje != None:
                        viajes.append(viaje.info)
                        viaje=viaje.sig
                act=act.sig
            return viajes
        else:
            return None
            
'''
g=grafo()
rdt = ciudad('Rosario del Tala')
cdu = ciudad('Concepcion del Uruguay')
ny = ciudad('Nogoya')
bs = ciudad('Basavilbaso')
mc = ciudad('Macia')
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