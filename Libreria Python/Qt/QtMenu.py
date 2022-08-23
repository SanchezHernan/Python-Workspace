# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 08:16:19 2018

@author: sanch
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.statusBar().showMessage('Loading...')
        self.setGeometry(300,300,200,200)
        self.setWindowTitle('StatusBar')
        self.show()
        
def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    