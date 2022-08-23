import sys
from PyQt4 import QtCore, QtGui

class QDataViewer(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        # Layout Init.
        self.setGeometry(650, 300, 600, 600)
        self.setWindowTitle('Data Viewer')
        self.quitButton = QtGui.QPushButton('QUIT', self)
        self.uploadButton = QtGui.QPushButton('UPLOAD', self)
        
        self.lineEdit = QtGui.QlineEdit()      
        hBoxLayout = QtGui.QHBoxLayout()
        hBoxLayout.addWidget(self.quitButton)
        hBoxLayout.addWidget(self.uploadButton)
        hBoxLayout.addWidget(self.lineEdit)
        self.setLayout(hBoxLayout)
        # Signal Init.
        self.connect(self.quitButton,   QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
        self.uploadButton.clicked.connect(self.showDialog)
        
    def showDialog(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
                '/home')
        
        f = open(fname, 'r')
        
        with f:        
            data = f.read()
            self.lineEdit.setText(data) 



def main():
    app = QtGui.QApplication(sys.argv)
    mw = QDataViewer()
    mw.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()