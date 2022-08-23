import sys
from PyQt4.QtGui import QApplication, QDialog
from PyQt4 import uic

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("comboBox.ui", self)
        self.botonEnviar.clicked.connect(self.getItem)
        #Agregar un nuevo item
        self.comboBox.addItem("C++")
        #Eliminar un item
        self.comboBox.removeItem(0)
        
    def getItem(self):
        item = self.comboBox.currentText()
        self.label.setText("Has seleccionado: "+ item)
    
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()