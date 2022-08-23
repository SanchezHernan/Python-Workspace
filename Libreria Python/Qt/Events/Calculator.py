# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:47:53 2018

@author: sanch
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        lcd = QtGui.QLCDNumber(self)
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        grid.addWidget(lcd, 0, 0, 1, 4)

        b1 = QtGui.QPushButton("1", self)
        b2 = QtGui.QPushButton("2", self)
        b3 = QtGui.QPushButton("3", self)
        b4 = QtGui.QPushButton("4", self)
        b5 = QtGui.QPushButton("5", self)
        b6 = QtGui.QPushButton("6", self)
        b7 = QtGui.QPushButton("7", self)
        b8 = QtGui.QPushButton("8", self)
        b9 = QtGui.QPushButton("9", self)
        b0 = QtGui.QPushButton("0", self)
        bCls = QtGui.QPushButton("Cls", self)
        bBck = QtGui.QPushButton("Bck", self)
        bClose = QtGui.QPushButton("Close", self)
        bMul = QtGui.QPushButton("*", self)
        bDiv = QtGui.QPushButton("/", self)
        bSus = QtGui.QPushButton("-", self)
        bSum = QtGui.QPushButton("+", self)
        bPnt = QtGui.QPushButton(".", self)
        bEq = QtGui.QPushButton("=", self)
        
        grid.addWidget(bCls, 1, 0)
        grid.addWidget(bBck, 1, 1)
        grid.addWidget(bClose, 1, 3)
        grid.addWidget(b7,2,0)
        grid.addWidget(b8, 2, 1)
        grid.addWidget(b9, 2, 2)
        grid.addWidget(bDiv, 2, 3)
        grid.addWidget(b4, 3, 0)
        grid.addWidget(b5, 3, 1)
        grid.addWidget(b6, 3, 2)
        grid.addWidget(bMul, 3, 3)
        grid.addWidget(b1, 4, 0)
        grid.addWidget(b2, 4, 1)
        grid.addWidget(b3, 4, 2)
        grid.addWidget(bSus, 4, 3)
        grid.addWidget(b0, 5, 0)
        grid.addWidget(bPnt, 5, 1)
        grid.addWidget(bEq, 5, 2)
        grid.addWidget(bSum, 5, 3)
        
        bCls.clicked.connect(self.buttonClicked)
        bBck.clicked.connect(self.buttonClicked)
        bClose.clicked.connect(self.buttonClicked)
        b7.clicked.connect(lcd.display(7))
        b8.clicked.connect(lcd.display(8))
        b9.clicked.connect(lcd.display(9))
        bDiv.clicked.connect(self.buttonClicked)
        b4.clicked.connect(self.buttonClicked)
        b5.clicked.connect(self.buttonClicked)
        b6.clicked.connect(self.buttonClicked)
        bMul.clicked.connect(self.buttonClicked)
        b1.clicked.connect(self.buttonClicked)
        b2.clicked.connect(self.buttonClicked)
        b3.clicked.connect(self.buttonClicked)
        bSus.clicked.connect(self.buttonClicked)
        b0.clicked.connect(self.buttonClicked)
        bPnt.clicked.connect(self.buttonClicked)
        bEq.clicked.connect(self.buttonClicked)
        bSum.clicked.connect(self.buttonClicked)
       
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()
        
    def buttonClicked(self):
       pass
            
        
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()