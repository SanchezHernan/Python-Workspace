import sys
from PyQt4.QtGui import QApplication, QDialog
from PyQt4 import uic

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("listWidget.ui", self)
        self.boton.clicked.connect(self.getItems)
        #Agregar un nuevo item
        self.listLeng.addItem("C++")
        #Eliminar un item
        #self.deleteItem("Python PHP")
        
    def contextMenuEvent(self, event):
        self.menu = QMenu(self)
        closeAction = QAction('Cerrar', self)
        closeAction.triggered.connect(lambda: self.renameSlot(event))
    
    '''    
    def deleteItem(self, leng):
        #Array para almacenar cada item objeto
        items = []
        #Recorrer item a item
        for x in range(self.listLeng.count()):
            item = self.listLeng.item(x)
            items.append(item)
        #este array almacena el texto de cada item
        labels = [i.text() for i in items]
        #Recorrer item a item el array labels
        for x in range(len(labels)):
            if labels[x] == leng:
                #Eliminar
                item = self.listLeng.indexFromItem(self.listLeng.item(x))
                self.listLeng.model().removeRow(item.row()) 
    '''
                
    def getItems(self):
        items = self.listLeng.selectedItems()
        #Array para guardar los items seleccionados
        selected = []
        if len(items) > 0:
            for x in range(len(items)):
                selected.append(self.listLeng.selectedItems()[x].text())
            self.label.setText("Seleccionados: "+"-".join(selected))
        else:
            self.label.setText("Ningun lenguaje seleccionado")
        
app=QApplication(sys.argv)
dialogo=Dialogo()
dialogo.show()
app.exec_()