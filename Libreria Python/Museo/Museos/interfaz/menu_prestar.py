# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, uic



menu = uic.loadUiType("interfaz/menu_prestar.ui")[0]
 
class prestarMuestra(QtGui.QDialog, menu):
    
    def __init__(self, lista_museos=None, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.lista_museos = lista_museos
        self.museo = None
        self.confirmar.clicked.connect(self.confirmar_museo)
        for museo in self.lista_museos:
            self.museos.addItem(museo.nombre)
        
    def confirmar_museo(self):
        self.museo = self.lista_museos[self.museos.currentIndex()]
        
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText("Prestama Exitoso")
        respuesta = msg.exec()
        self.hide() 
    