# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 22:08:43 2018

@author: Sanchez Hernan
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")
        
        hbox=QtGui.QHBoxLayout()
        hbox.addStretch(6)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        
        vbox=QtGui.QVBoxLayout()
        vbox.addStretch(10)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        
        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Buttons')
        self.show()
        
def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()      