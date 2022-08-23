# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 13:32:17 2018

@author: sanch
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)
        
        exitAction = QtGui.QAction(QtGui.QIcon('../Icons/exit.ico'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        
        anotherAction = QtGui.QAction(QtGui.QIcon('../Icons/web.png'), 'Navegate', self)
        anotherAction.setShortcut('Alt+N')
        anotherAction.setStatusTip('Navegation begins')
        anotherAction.triggered.connect(self.isFullScreen)
        
        anilloAction = QtGui.QAction(QtGui.QIcon('../Icons/anillo.png'), 'Casorio', self)
        anilloAction.setShortcut('Alt+A')
        anilloAction.setStatusTip('Casate conmigo mamuh!')
        anilloAction.triggered.connect(self.close)
        
        self.statusBar()
        
        menubar = self.menuBar()
        menuFile = menubar.addMenu('&File')
        menuFile.addAction(anotherAction)
        menuFile.addAction(anilloAction)
        menuFile.addAction(exitAction)
        
        
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Hola amtituh')
        self.setWindowIcon(QtGui.QIcon('../Icons/cool.png'))
        self.show()
        
def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()      
    
if __name__ == '__main__':
    main()