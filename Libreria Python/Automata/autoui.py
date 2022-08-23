import sys
from automata import Automata
from PyQt4.QtGui import QApplication, QDialog
from PyQt4 import uic


class Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("automata.ui", self)
        self.pushButton.clicked.connect(self.analizar)
        self.texto.        
        
    def analizar(self, automata):
        if automata.cadenaValida():
            
        
app = QApplication(sys.argv)
dialogo = Dialog()
dialogo.show()
app.exec_()

tabla = [
[1,2],[3,4],[3,0],[1,5],[7,2],[6,0],[7,7],[6,6]
]
estado = 0          
cadena = "bababaaba"

if not cadenaIncorrecta(cadena):
    automata = Automata(tabla, cadena, estado)
    if automata.cadenaValida():
        print('la cadena es valida')
    else:
        print('la cadena no es valida')
else:
    print('la cadena posee caracteres invalidos')

    