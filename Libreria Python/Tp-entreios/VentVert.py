# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 17:56:35 2017

@author: Blanc
"""

from PyQt4 import QtGui, QtCore, uic
#from CargarVert import *
from Archivos import *
import geocoder as gc
import os
from TDA_Grafo import *
ruta = os.path.realpath('ArchER/Vertices.dat')



  
class VentVert(QtGui.QDialog):
    def __init__(self,parent=None, g):
        QtGui.QWidget.__init__(self,parent)
        #self.ui = Ui_DialogVert()        
        #self.ui.setupUi(self)
        uic.loadUi('interfaces/CargarVert.ui', self)
        QtCore.QObject.connect(self.BCancelar, QtCore.SIGNAL('clicked()'),self.cerrar)
        QtCore.QObject.connect(self.BAgregarVert, QtCore.SIGNAL('clicked()'), self.agregarCiudad)
        self.cargarGrafoVert(ruta)
    
    def cerrar(self):
        self.close() 
        
    def validar(self):
        if(len(self.ciudad.text())==0):
            return False
        elif(len(self.CP.text())==0):
            return False
        return True
            
    def crearCiudad(self):
        return ciudad(self.ciudad.text(), self.CP.text())
        
    
    def agregarCiudad(self):
        if self.validar():
            archivo = abrir(ruta)
            geopos = gc.geocoder(reg.Ciudad)
            city = ciudad(self.ciudad.text(), self.CP.text(), geopos['lat'], geopos['lng'])
            if g.altaVertice(city):
                pass
            '''
            if self.grafo.altaVertice(city):
                reg.Ciudad = self.ciudad.text()
                reg.CP = self.CP.text()
                reg.id = len(archivo)
                geopos = gc.geocoder(reg.Ciudad)
                reg.Latitud = geopos['lat']
                reg.Longitud = geopos['lng']
            '''
            
            
        self.ciudad.setText('')
        self.CP.setText('')
        
    def cargarGrafoVert(self, archivoVertices):
        ciud = ciudad(None, None)
        vertices=abrir(archivoVertices)
        for i in range(0,len(vertices)):
            x=leer(vertices,i)
            ciud.setNombre(x.Ciudad)
            ciud.setCP(x.CP)
            ciud.setIdCiudad(x.getId())
            self.grafo.altaVertice(ciud)
        cerrarArch(vertices)
    
    

    '''    
    def validar(self):
        if(len(self.ciudad.text())==0):
            return None
        elif(len(self.CP.text())==0):
            return None
        else:
            nodo = registroVertice()
            nodo.Ciudad = self.ciudad.text()
            nodo.CP = self.CP.text()
            nodo.Provincia = "Entre Rios"
            return nodo
    
    def createPath(self,nodo):
        return '%s' % (nodo.Ciudad) + ' Entre Rios'
        
    def cargar(self):
        resultado = self.validar()
        if(resultado != None): 
            arVertices = abrir(ruta)
            resultado.id = len(arVertices)
            geopos = gc.geocoder(self.createPath(resultado))
            resultado.Latitud = geopos['lat']
            resultado.Longitud = geopos['lng']
            guardar(arVertices, resultado)
            cerrarArch(arVertices)
        self.ciudad.setText('')
        self.CP.setText('')
    '''
      
def crearVentVertice(g):
    FormVert = VentVert(g)
    FormVert.show()
    FormVert.exec_()