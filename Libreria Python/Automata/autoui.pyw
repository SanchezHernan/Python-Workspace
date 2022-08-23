import sys
from automata import Automata, cadenaIncorrecta
from PyQt4.QtGui import QApplication, QDialog
from PyQt4 import uic


class Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("automata.ui", self)
        self.setWindowTitle('Automata Finito Deterministico')
        self.pushButton.clicked.connect(self.analizar)
          
        
    def analizar(self, automata):
        self.texto.setText('')
        tabla = [[1,2],[3,4],[3,0],[1,5],[7,2],[6,0],[7,7],[6,6]
        ]
        automata = Automata(tabla, 0)
        txt = self.lineEdit.text()
        if not cadenaIncorrecta(txt):
            automata.setCadena(txt)
            if automata.cadenaValida():
                self.texto.setText('cadena valida')
            else:
                self.texto.setText('cadena invalida')
        else:
            self.texto.setText('cadena incorrecta')


        
app = QApplication(sys.argv)
dialogo = Dialog()
dialogo.show()
app.exec_()


    