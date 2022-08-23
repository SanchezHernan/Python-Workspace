import sys, re
from PyQt4.QtGui import QApplication, QDialog, QMessageBox
from PyQt4 import uic

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("validacion.ui", self)
        self.Nombre.textChanged.connect(self.validar_nombre)
        self.Email.textChanged.connect(self.validar_email)
        self.boton.clicked.connect(self.validar_formulario)
        
    def validar_nombre(self):
        nombre = self.Nombre.text()
        validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', nombre, re.I)
        if nombre == "":
            self.Nombre.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.Nombre.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.Nombre.setStyleSheet("border: 1px solid green;")
            return True

    def validar_email(self):
        email = self.Email.text()
        validar = re.match('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$', email, re.I)
        if email == "":
            self.Email.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.Email.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.Email.setStyleSheet("border: 1px solid green;")
            return True
            
    def validar_formulario(self):
        if self.validar_nombre() and self.validar_email():
            QMessageBox.information(self, "Formulario Correcto", "Validacion correcta", QMessageBox.Discard)
            
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "Validacion incorrecta", QMessageBox.Discard)
            
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()