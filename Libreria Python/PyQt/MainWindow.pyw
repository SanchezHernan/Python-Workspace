import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import uic
import ctypes #GetSystemMetrics

#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QtGui.QMainWindow):
    #Metodo constructor de la clase
    def __init__(self):
        #iniciar el objeto QMainWindow
        super(Ventana, self).__init__()
        uic.loadUi("main.ui",self)
        #Cargar la configuracion del archivo .ui en el objeto
        self.setWindowTitle("Tirulo Cambiado")
        #fijar el tamano minimo de la ventana
        self.setMinimumSize(500, 500)
        #fijar el tamano maximo
        self.setMaximumSize(500,500)
         #Mover la ventana y centrarla en el escritorio
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left = (resolucion_ancho / 2) - (self.frameSize().width() / 2)
        top = (resolucion_alto / 2) - (self.frameSize().height() / 2)
        self.move(left, top)
        #Desactivar la ventana
        #self.setEnabled(False)
        #Asignar un tipo de fuente
        qfont = QtGui.QFont("Arial",12,QtGui.QFont.Bold)
        self.setFont(qfont)
        #Asignar un tipo de cursor
        self.setCursor(QtCore.Qt.SizeAllCursor)
        #Asignar estilos CSS
        #self.setStyleSheet("background-color: #500; color: #fff;")
        self.boton.setStyleSheet("background-color: #035; color: #fff; font-size: 14px;")       
        
    def showEvent(self, event):
        self.welcomeLabel.setText("Bienvenido!!") 
        
    def closeEvent(self, event):
        resultado = QtGui.QMessageBox.question(self, "Salir...",
        "Seguro que quieres cerrar la aplicacion?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if resultado == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def moveEvent(self, event):
        x = str(event.pos().x())
        y = str(event.pos().y())
        self.positionLabel.setText("x: "+ x + " y: "+ y)
        
#Instancia para iniciar una aplicacion
app = QtGui.QApplication(sys.argv)
#crear ventana
_ventana = Ventana()
#mostrar ventana
_ventana.show()
#ejecutar aplicacion
app.exec_()

        