# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:33:33 2017

@author: Blanc
"""

import sys
from PyQt4 import QtGui
from Menu import *
from VentMapa import *
from VentArista import *
from VentVert import * 
from TDA_Grafo import *
import geocoder as gc

#cargo los primeros vertices 
from Archivos import *
import os
ruta = os.path.realpath('ArchER/Vertices.dat')
aristas = os.path.realpath('ArchER/Aristas.dat')


class MenuPrinc(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.grafo = grafo()
        
        self.cargarCiudades() #carga por primera vez las ciudades
        self.cargarGrafo(ruta, aristas)
        
        QtCore.QObject.connect(self.ui.BVerMapa, QtCore.SIGNAL('clicked()'),self.abrirMapa)
        QtCore.QObject.connect(self.ui.BAgArista, QtCore.SIGNAL('clicked()'),self.agregarAris)
        QtCore.QObject.connect(self.ui.BAgVert, QtCore.SIGNAL('clicked()'),self.agregarVert)
        self.ui.btnRefresh.clicked.connect(self.cargarCiudades)
        
        
    def abrirMapa(self):
        crearMapa()
      

    def agregarAris(self):
        #self.guardarEnArchivo()
        crearVentArista()

    def agregarVert(self):
        crearVentVertice(self.grafo)
        #g.listarGrafo()
         
        
    def createPath(self, ciudad):
        return '%s' % ciudad + ' Entre Rios'

           
    def cargarGrafo(self, archivoVertices, archivoAristas):
        ciud = ciudad(None, None)
        vertices=abrir(archivoVertices)
        aristas=abrir(archivoAristas)
        for i in range(0,len(vertices)):
            x=leer(vertices,i)
            ciud.setNombre(x.Ciudad)
            ciud.setCP(x.CP)
            ciud.setIdCiudad(x.getId())
            print(ciud.getNombre())
            self.grafo.altaVertice(ciud)
        cerrarArch(vertices)
        for i in range(0,len(aristas)):
            x=leer(aristas,i)
            v = viaje(x.ciudOr, x.ciudDest, x.importe, x.distancia)
            self.grafo.generarArco(v)
        cerrarArch(aristas)    
        
    def cargarCiudades(self): 
        self.ui.listView.clear()
        vertices=abrir(ruta)  
        for i in range(0,len(vertices)):
            x=leer(vertices,i) 
            self.ui.listView.addItem(self.createPath(x.Ciudad))  
        cerrarArch(vertices) 
        
    def guardarEnArchivo(self):
        regv = registroVertice()
        rega = registroArista()
        arVertices = abrir(ruta)
        arAristas = abrir(aristas)
        act = self.grafo.cab
        while act != None:
            #si el idCiudad es None significa que no ha sido guardado en el archivo
            if act.ciud.getIdCiudad() == None:
                lenver = len(arVertices)
                act.ciud.setIdCiudad(lenver)
                regv.Ciudad = act.ciud.getNombre()
                regv.CP = act.ciud.getCP()
                regv.Provincia = 'Entre Rios'
                geopos = gc.geocoder(self.createPath(reg.Ciudad))
                regv.Latitud = geopos['lat']
                regv.Longitud = geopos['lng']
                guardar(arVertices, regv)
            if (act.cab != None):
                aux = act.cab
                while aux != None:
                    if aux.info.getIdViaje() == None:
                        lenar = len(arAristas)
                        aux.info.setIdViaje(lenar)
                        rega.id = lenar
                        rega.ciudOr = aux.info.getOrigen()
                        rega.ciudDest = aux.info.getDestino()
                        rega.distancia = aux.info.getDistancia()
                        rega.importe = aux.info.getImporte()
                        guardar(arAristas, rega)
                    aux=aux.sig
            act=act.sig
        cerrarArch(arVertices)
        cerrarArch(arAristas)
        
        
        
'''
    while (opc != 0):
        if(opc == 1):
            cargarCiudad(g, vertices, input("Cargue la ciudad: "))
        elif(opc == 2):
            cargarViaje(g, aristas, input("Ciudad origen: "), input("ciudad destino: "), int(input('distancia: ')), int(input('importe: ')))
        elif(opc == 3):
            listarGrafo(g)
            print()
        elif(opc == 0):
            i = 10
        opc = mostrarMenu()        
'''
if(__name__=="__main__"):
    app = QtGui.QApplication(sys.argv)
    principal = MenuPrinc()
    principal.show()
    app.exec_()
    print('')
    principal.grafo.listarGrafo()
