# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 15:01:58 2018

@author: sanch
"""

import sys 
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        lbl1=QtGui.QLabel('ZetCode', self)
        lbl1.move(15,10)
        
        lbl2=QtGui.QLabel('tutorials', self)
        lbl2.move(35,40)

        lbl3=QtGui.QLabel('for programmers', self)
        lbl3.move(55,70)        
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('La ventanitax')
        self.show()

def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()      
        