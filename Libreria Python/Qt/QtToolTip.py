# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 22:48:30 2018

@author: sanch
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()        
        self.initUI()
    
    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn=QtGui.QPushButton('Aceptar', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(100,150)
        
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Tooltips')
        self.show()
        
def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
    
if __name__== '__main__':
    main()