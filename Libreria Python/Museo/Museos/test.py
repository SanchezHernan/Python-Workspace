    # -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, uic, QtCore

from interfaz.dialog import DialogoMuseo
from interfaz.mapa import DialogMapa
from interfaz.menu_muestra import Menu_Muestra



def orden_nombre(item):
    return item.nombre


menu = uic.loadUiType("interfaz/main.ui")[0] 

#Heredamos de las clases QMainWindow y del formulario que realizamos
class Ventana(QtGui.QMainWindow,menu):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.lista_museos = []
        self.ordenar.clicked.connect(self.ordenar_museo)
        self.agregar.clicked.connect(self.abrir_museo)
        self.mapa.clicked.connect(self.abrir_mapa)
        self.eliminar.clicked.connect(self.eliminar_museo)
        self.ver.clicked.connect(self.ver_museo)
        """ 
        def cambiar_texto(self):
            valor = self.text_copiar.text()
            self.text_nombre.setText(valor)
        """
        
        """        
        self.visor.clicked.connect(self.abrir_mapa)
        #self.b_vehiculo.clicked.connect(self.ordenar)        
        self.listap = [p.Persona("walter","bel")]
        self.listav = []
        self.listae = []
        for i in range(0,10):
            self.listae.append(e.Estacionamiento(i))
        """
    def abrir_mapa(self):
        lista = []
        for museo in self.lista_museos:
                lista.append(museo.direccion + " concepcion del uruguay" )
        dial = DialogMapa(lista)
        dial.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dial.setModal(True)        
        dial.exec_()
        
    def eliminar_museo(self):
        fila = self.tabla.currentRow()
        if(fila>=0):
            self.tabla.removeRow(fila)
            self.lista_museos.pop(fila)
        
    def ver_museo(self):
        dial = Menu_Muestra(self.lista_museos[int(self.tabla.currentRow())], self.lista_museos)
        dial.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dial.setModal(True)        
        dial.exec_()
        self.lista_museos.sort(key=orden_nombre)
    
    def ordenar_museo(self):
        self.lista_museos.sort(key=orden_nombre)
        self.tabla.setRowCount(0)
        for museo in self.lista_museos:
            self.tabla.insertRow(self.tabla.rowCount())
            self.tabla.setItem(self.tabla.rowCount()-1, 0, 
                               QtGui.QTableWidgetItem(museo.nombre))        
            self.tabla.setItem(self.tabla.rowCount()-1, 1, 
                               QtGui.QTableWidgetItem(museo.direccion))
    
    def abrir_museo(self):
        dial = DialogoMuseo()
        dial.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dial.setModal(True)        
        dial.exec_()
        self.tabla.insertRow(self.tabla.rowCount())
        self.tabla.setItem(self.tabla.rowCount()-1, 0, 
                           QtGui.QTableWidgetItem(dial.museo.nombre))        
        self.tabla.setItem(self.tabla.rowCount()-1, 1, 
                           QtGui.QTableWidgetItem(dial.museo.direccion))
            
        self.lista_museos.append(dial.museo)
        
        """
        self.t_persona.setRowCount(0)
        self.t_persona.insertRow(self.t_persona.rowCount())
        self.t_persona.setItem(self.t_persona.rowCount()-1, 0, 
                               QtGui.QTableWidgetItem(self.lista[0]))
        self.t_persona.setItem(self.t_persona.rowCount()-1, 1, 
                               QtGui.QTableWidgetItem(self.lista[1]))
        self.t_persona.setItem(self.t_persona.rowCount()-1, 2, 
                               QtGui.QTableWidgetItem(self.lista[2]))
        print(dial.museo.nombre)
        """
        
        
app = QtGui.QApplication(sys.argv)
principal = Ventana()
principal.show()
app.exec_()