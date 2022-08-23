# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 06:37:38 2018

@author: sanch
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.resize(250,150)
        self.center()
        self.setWindowTitle('Center')
        self.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
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
    
if __name__ == '__main__':
    main()