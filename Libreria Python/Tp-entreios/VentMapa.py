# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 17:59:50 2017

@author: Blanc
"""

from PyQt4 import QtGui
from Mapa import *
from TDA_Grafo import *
from Archivos import *
import os

rutaVert = os.path.realpath('ArchER/Vertices.dat')
rutaAris = os.path.realpath('ArchER/Aristas.dat')
g = grafo()
GrafoA = grafo()
NodoV = nodoVertice()
lista_Ciud = []

class VentMapa(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Mapa()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.BCerrar, QtCore.SIGNAL('clicked()'),self.cerrar)
        QtCore.QObject.connect(self.ui.BMostTodo, QtCore.SIGNAL('clicked()'),self.mostrarTodos)
    
    def cerrar(self):
        self.close()

    def mostrarTodos(self):
        vertices = abrir(rutaVert)
        for i in range (0,len(vertices)):
            x=leer(vertices,i)
            g.altaVertice(x.Ciudad+", Entre Rios", 1234)
        cerrarArch(vertices)
        self.cargarGrafo(GrafoA, rutaVert, rutaAris)
        center ="center=villaguay entre rios"
        zoom = "&zoom=7"
        size = "&size=679x468"
        lista_Ciud = g.tomarCiud
        marcas = "|"
        marcas = marcas.join(lista_Ciud)
        markers = "&markers=" + "color:blue|"+ marcas
        lista_Cam = GrafoA.tomarCam
        auxPath = "|"
        auxPath = auxPath.join(lista_Cam)
        path="&path="+auxPath
        imgformat = "&format=png"
        maptype="&maptype=roadmap"
        sensor = "&sensor=false"
        self.ui.webView.load(QtCore.QUrl("https://maps.googleapis.com/maps/api/staticmap?"+center+zoom
                        +size+markers+path+imgformat+maptype+sensor))
        print("https://maps.googleapis.com/maps/api/staticmap?"+center+zoom
                        +size+markers+path+imgformat+maptype+sensor)
                        
        
    def cargarGrafo(self,graph, archivoVertices, archivoAristas):
        vertices=abrir(archivoVertices)
        aristas=abrir(archivoAristas)
        for i in range(0,len(vertices)):
            x=leer(vertices,i)
            graph.altaVertice(x.Ciudad, 1234)
        cerrarArch(vertices)
        for i in range(0,len(aristas)):
            x=leer(aristas,i)
            graph.generarArco(x.ciudOr, x.ciudDest,int(x.distancia), int(x.importe))
        cerrarArch(aristas)
                        
def crearMapa():
    Mapa = VentMapa()
    Mapa.show()
    Mapa.exec_()