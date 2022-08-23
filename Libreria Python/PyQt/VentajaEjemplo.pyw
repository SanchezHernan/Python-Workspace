import sys
from PyQt4 import QtGui, QtCore

#Clase heredada de QMainWindow (Constructor de ventanas)
class ventanaEjemplo(QtGui.QWidget):
    #Metodo constructor de la clase
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Ventana Ejemplo')
        qbtn = QtGui.QPushButton('Cerrar', self)
        qbtn.setGeometry(10, 10, 70, 40)
        #self.connect(qbtn, QtCore.SIGNAL('clicled()'), QtGui.qApp, QtCore.SLOT('quit()'))
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #qbtn.resize(qbtn.sizeHint())
                
        
        
app = QtGui.QApplication(sys.argv)
vent = ventanaEjemplo()
vent.show()
sys.exit(app.exec_())