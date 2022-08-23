import sys
from QSIterativo import quickSortIt, listar
from PyQt4 import QtGui
from PyQt4 import uic


vec = []

class Dialogo(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setWindowTitle("Cuadro de dialogo")
        uic.loadUi("QQS.ui", self)   
        self.pushButton.clicked.connect(self.agregar)        
        self.botonOrdenar.clicked.connect(self.ordenar)        
        
    def agregar(self):
        num = int(self.lineEdit.text())
        vec.append(num)
        self.lineEdit.clear()
        if self.label2.text() == '':
            self.label2.setText('Numeros: ' + str(num))
        else:
            nums = self.label2.text()
            nums += ', '+str(num)
            self.label2.setText(nums)
            
        
    def ordenar(self):
        if len(vec) > 0:           
            quickSortIt(vec, 0, len(vec)-1)   
            nums=listar(vec)
            self.label2.setText('Numeros: ' + nums)
        else:
            self.label2.setText('No ha ingresado ningun numero')
            
app = QtGui.QApplication(sys.argv)
ventana = Dialogo()
ventana.show()
app.exec_()   