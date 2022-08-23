# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 17:48:23 2017

@author: Blanc
"""

import os
dir = os.path.dirname(__file__)
ruta = os.path.realpath('ArchER/Aristas.dat')


from PyQt4 import QtGui, uic
from CargarCam import *
from Archivos import *
import hervaisen 


Nodo = registroArista()

class VentAris(QtGui.QDialog):
    
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent,)
        #self = Ui_DialogCarga()
        #self.setupUi(self)
        uic.loadUi('interfaces/CargarCam.ui', self)
        self.distanciaActual = 0   
        
        self.cargarComboBox(self.ciudadOrigen)
        self.cargarComboBox(self.ciudadDestino)
        
        QtCore.QObject.connect(self.BCancelar, QtCore.SIGNAL('clicked()'),self.cerrar)
        QtCore.QObject.connect(self.bAgregarAris, QtCore.SIGNAL('clicked()'),self.cargar)
        self.cargarGeoPos()
        self.ciudadOrigen.currentIndexChanged.connect(self.cargarGeoPos)
        self.ciudadDestino.currentIndexChanged.connect(self.cargarGeoPos)
        
    def createPath(self,nodo):
        return '%s, %s' % (nodo.Ciudad, nodo.Provincia)

    def cargarComboBox(self, comboBox): 
        vertices=abrir(os.path.realpath('ArchER/Vertices.dat'))  
        for i in range(0,len(vertices)):
            x=leer(vertices,i) 
            comboBox.addItem(self.createPath(x),i)  
        cerrarArch(vertices) 
    
    def cargarGeoPos(self): 
        idOrigen = self.ciudadOrigen.itemData(self.ciudadOrigen.currentIndex())
        idDestino = self.ciudadDestino.itemData(self.ciudadDestino.currentIndex())
        vertices=abrir(os.path.realpath('ArchER/Vertices.dat'))   
        origen=leer(vertices,idOrigen)   
        destino=leer(vertices,idDestino)   
        cerrarArch(vertices) 
        self.distanciaActual = hervaisen.geo_distance(
            origen.Longitud,
            origen.Latitud,
            destino.Longitud,
            destino.Latitud)
        self.mostrarDistanciaEstimada()
         
                
    def mostrarDistanciaEstimada(self):
        self.distancia.setText("distancia estimada: %s" % (self.distanciaActual) )
    
    def cerrar(self):
        self.close()
             
    def cargar(self):
        vertices=abrir(os.path.realpath('ArchER/Vertices.dat'))
        idOrigen = self.ciudadOrigen.itemData(self.ciudadOrigen.currentIndex())
        aux=leer(vertices,idOrigen)
        Nodo.ciudOr=aux.Ciudad
        idDestino = self.ciudadDestino.itemData(self.ciudadDestino.currentIndex())
        aux = leer(vertices,idDestino)
        Nodo.ciudDest = aux.Ciudad
        cerrarArch(vertices)
        if(len(self.distancia.text())!=0):
            Nodo.distancia = self.distanciaActual
        if(len(self.empresa.text())!=0):
            Nodo.empresa = self.empresa.text()
        if(len(self.importe.text())!=0):
            Nodo.importe = self.importe.text()
        arAristas=abrir(ruta)
        guardar(arAristas, Nodo)
        cerrarArch(arAristas)
        #else:
            #imprimir que no se pudo
        self.empresa.setText('')
        self.importe.setText('')

def crearVentArista():
    FormVert = VentAris()
    FormVert.show()
    FormVert.exec_()
    grafo.listarGrafo()