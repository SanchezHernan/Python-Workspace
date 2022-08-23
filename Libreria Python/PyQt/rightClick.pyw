import sys
from PyQt4.QtCore import Qt
from PyQt4 import QtGui


class MyWidget(QtGui.QWidget):


    def __init__(self):
        super(MyWidget, self).__init__()

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print("Left Button Clicked")
        elif QMouseEvent.button() == Qt.RightButton:
            #do what you want here
            print("Right Button Clicked")

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    mw = MyWidget()
    mw.show()
    sys.exit(app.exec_())