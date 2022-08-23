import sys
from PyQt4.QtGui import QApplication, QDialog
from PyQt4 import uic

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('sliders.ui',self)
        
        #Horizantal slider
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.valueChanged.connect(self.getValueHorizontal)
        
        #Vertical slider
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(1000)
        self.verticalSlider.setSingleStep(10)
        self.verticalSlider.setValue(500)
        self.verticalSlider.valueChanged.connect(self.getValueVertical)
        
    def getValueHorizontal(self):
        value = self.horizontalSlider.value()
        self.labelH.setText(str(value))
        
    def getValueVertical(self):
        value = self.verticalSlider.value()
        '''aqui'''        
        self.labelV.setText(str(value))
        
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()