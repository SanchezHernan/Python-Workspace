# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 10:29:56 2018

@author: sanch
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.statusBar().showMessage('Ready')
        exitAction = QtGui.QAction(QtGui.QIcon('../Icons/exit.ico'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        self.statusBar()
        
        '''
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        '''                        
        #resumido lo de arriba
        self.menuBar().addMenu('&File').addAction(exitAction)
    
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('MenuBar')
        self.show()
        
def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()