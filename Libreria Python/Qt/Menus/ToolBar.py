# -*- coding: utf-8 -*-
"""
This program creates a toolbar.

@author: Hernan Sanchez
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        exitAction = QtGui.QAction(QtGui.QIcon('../Icons/exit.ico'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        anotherAction = QtGui.QAction(QtGui.QIcon('../Icons/web.png'), 'Salir', self)
        anotherAction.setShortcut('Ctrl+S')
        anotherAction.triggered.connect(QtGui.qApp.quit)
        
        self.toolbar = self.addToolBar('Exit (Ctrl+Q)')
        self.toolbar2 = self.addToolBar('Salir (Ctrl+S)')
        self.toolbar.addAction(exitAction)
        self.toolbar2.addAction(anotherAction)
        
        
        
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Toolbar')
        self.show()
        
def main():
     app = QtGui.QApplication(sys.argv)
     ex=Example()
     sys.exit(app.exec_())

if __name__ == '__main__':
    main()    