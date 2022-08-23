# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic

#import entidades.museo
from entidades.museo import Museo

menu = uic.loadUiType("interfaz/museo.ui")[0]
 
class DialogoMuseo(QtGui.QDialog, menu):
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.museo = None
        self.cargar.clicked.connect(self.cargar_museo)
        
    def cargar_museo(self):
        if len(self.nombre.text().strip())>0 and len(self.direccion.text().strip())>0:
            self.museo = Museo()
            self.museo.nombre = self.nombre.text()
            self.museo.direccion = self.direccion.text()
            self.hide() 
        else:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setText("Debe completar los campos")
            #msg.setStandardButtons(QtGui.QMessageBox.Ok|QtGui.QMessageBox.Yes|QtGui.QMessageBox.No|QtGui.QMessageBox.Save)
            respuesta = msg.exec()
            
        
        
        
    """    
    def modificar(self):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Question)
        msg.setText("Esta seguro que dese modificar")
        msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        #msg.buttonClicked.connect(self.mensaje)
        retval = msg.exec_()
        if retval==1024:
            persona = entidad.persona.Persona(self.t_nom.text(), self.t_ape.text(), 
                                                   self.t_dni.text())                        
            self.persona = persona
            self.hide()
    """
    """    
    def mensaje(self, msj):
        print (msj.text())
    """
