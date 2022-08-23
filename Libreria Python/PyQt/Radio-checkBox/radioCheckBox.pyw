import sys
from PyQt4.QtGui import QApplication, QDialog
from PyQt4 import uic

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("radio-checkBox.ui", self)
        self.radio_value()
        self.boton.clicked.connect(self.radio_value)
        self.checkbox_state()
        self.boton.clicked.connect(self.checkbox_state)

    def radio_value(self):
        if self.python.isChecked():
            self.labelLeng.setText("Python ha sido seleccionado")
        elif self.php.isChecked():
            self.labelLeng.setText("PHP ha sido seleccionado")
        elif self.java.isChecked():
            self.labelLeng.setText("Java ha sido seleccionado")
        elif self.pascal.isChecked():
            self.labelLeng.setText("Pascal? En serio?")
        else:
            self.labelLenguaje.setText("No hay seleccionado ningún lenguaje")
   
    def checkbox_state(self):
        if self.terminos.isChecked():
            self.labelTerminos.setText("Has aceptado los teminos")
        else:
            self.labelTerminos.setText("No has aceptado los terminos")
              
     
 
   
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()