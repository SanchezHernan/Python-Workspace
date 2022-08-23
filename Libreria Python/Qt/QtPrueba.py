# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 19:08:43 2018

@author: sanch
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('Icons/web.png'))
        self.show()       
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()