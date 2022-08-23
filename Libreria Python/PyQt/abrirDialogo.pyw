import sys
from PyQt4 import QtGui
from PyQt4 import uic
 
class Dialogo(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.resize(300,300)
        self.setWindowTitle("Cuadro de dialogo")
        self.etiqueta = QtGui.QLabel(self)
        uic.loadUi("styleDialog.ui", self)
        
class Ventana(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(600, 600)
        self.setWindowTitle("Ventana Principal")
        self.btn = QtGui.QPushButton(self)
        self.btn.setText("Abrir cuadro de dialogos")
        self.btn.resize(200, 30)
        self.dialogo = Dialogo()
        self.btn.clicked.connect(self.abrirDialogo)
    
    def abrirDialogo(self):
        self.dialogo.etiqueta.setText("Dialogo abierto desde la ventana principal")
        self.dialogo.exec_()
        
    
app = QtGui.QApplication(sys.argv)
ventana = Ventana()
ventana.show()
app.exec_()