# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic

#import entidades.museo
#from entidades.museo import Museo
from datetime import date
from entidades.pintura import Pintura
from entidades.escultura import Escultura
from entidades.dinosaurio import Dinosaurio

menu = uic.loadUiType("interfaz/guardar_muestra.ui")[0]
 
class guardarMuestra(QtGui.QDialog, menu):
    
    def __init__(self, museo, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.museo = museo
        self.anio_ingreso.setDate(date.today())
        self.guardar.clicked.connect(self.cargar_muestra)
        self.combobox.currentIndexChanged.connect(self.habilitar)
    
    def cargar_muestra(self):
        if(self.combobox.currentIndex()==0):
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Debe Seleccionar un Tipo de Muestra")
            #msg.setStandardButtons(QtGui.QMessageBox.Ok|QtGui.QMessageBox.Yes|QtGui.QMessageBox.No|QtGui.QMessageBox.Save)
            respuesta = msg.exec()
            """
            if(respuesta==QtGui.QMessageBox.Ok):
                print("presiono boton OK")
            elif((respuesta==QtGui.QMessageBox.Save)):
                print("presiono boton guardar")
            """
        elif (self.combobox.currentIndex()==1):
            p = Pintura()
            p.codigo = self.codigo.text()
            p.anio_ingreso = self.anio_ingreso.date().toString("dd-MM-yyyy")
            p.replica = self.replica.isChecked()
            
            self.museo.muestras.append(p)
            self.hide()
        elif (self.combobox.currentIndex()==2):
            e = Escultura()
            e.peso = int(self.peso.text())
            e.codigo = self.codigo.text()
            
            e.anio_ingreso = self.anio_ingreso.date().toString("dd-MM-yyyy")
            self.museo.muestras.append(e)
            self.hide()
        elif (self.combobox.currentIndex()==3):
            d = Dinosaurio()
            d.especie = self.especie.text()
            d.codigo = self.codigo.text()
            
            d.anio_ingreso = self.anio_ingreso.date().toString("dd-MM-yyyy")
            self.museo.muestras.append(d)
            self.hide()
            
    def habilitar(self):
        if (self.combobox.currentIndex()==1):
            self.caja.setEnabled(True)
            self.peso.setEnabled(False)
            self.especie.setEnabled(False)
        elif (self.combobox.currentIndex()==2):
            self.caja.setEnabled(False)
            self.peso.setEnabled(True)
            self.especie.setEnabled(False)
        elif (self.combobox.currentIndex()==3):
            self.especie.setEnabled(True)
            self.caja.setEnabled(False)
            self.peso.setEnabled(False)
            

        """
        self.museo = entidades.museo.Museo()
        self.museo.nombre = self.nombre.text()
        self.museo.direccion = self.direccion.text()
        self.hide() 
        """