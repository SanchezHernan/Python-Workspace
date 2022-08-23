# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:21:13 2018

@author: sanch
"""

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30,50)
        
        btn2 = QtGui.QPushButton("Button2", self)
        btn2.move(150,50)
        
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setGeometry(300,300,250,160)
        self.setWindowTitle('Event Sender')
        self.show()
        
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()