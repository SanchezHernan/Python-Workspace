import sys
from PyQt4.QtGui import QApplication, QMenu, QMainWindow, QAction, QCursor, QMessageBox,QIcon
from PyQt4 import uic

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("rightClick.ui", self)
        
    def contextMenuEvent(self, event):
        self.menu = QMenu(self)
        closeAction = QAction('Cerrar', self)
        closeAction.triggered.connect(lambda: self.renameSlot(event))
        
        
        
    '''    
    def contextMenuEvent(self, event):
        self.menu = QMenu(self)
        renameAction = QAction('Rename', self)
        renameAction.triggered.connect(lambda: self.renameSlot(event))
        self.menu.addAction(renameAction)
        # add other required actions
        self.menu.popup(QCursor.pos())
    
    def renameSlot(self, event):
        print("renaming slot called")
        # get the selected row and column
        row = self.tableWidget.rowAt(event.pos().y())
        col = self.tableWidget.columnAt(event.pos().x())
        # get the selected cell
        cell = self.tableWidget.item(row, col)
        # get the text inside selected cell (if any)
        cellText = cell.text()
        # get the widget inside selected cell (if any)
        widget = self.tableWidget.cellWidget(row, col)        
    '''          

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()