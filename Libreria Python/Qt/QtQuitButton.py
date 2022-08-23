# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 23:28:38 2018

@author: sanch
"""

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()        
        self.initUI()
    
    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn=QtGui.QPushButton('Aceptar', self)
        btn.setToolTip('No hace nada <b>AUN</b>')
        btn.resize(btn.sizeHint())
        btn.move(150,50)
        
        qbtn = QtGui.QPushButton('Salir', self)
        qbtn.setToolTip('Pulsa para cerrar la ventana')
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)        
        
        self.setWindowTitle('La ventanita')
        self.setGeometry(300, 300, 200, 200)
        self.show()
        
        
    def closeEvent(self, event):
        reply=QtGui.QMessageBox.question(self, 'Advertencia',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
        
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        elif reply == QtGui.QMessageBox.No:
            event.ignore()
            
    
        
            
        
def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
    
if __name__== '__main__':
    main()