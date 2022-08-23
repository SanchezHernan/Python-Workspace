import sys, time
from PyQt4.QtGui import QApplication, QDialog, QTreeWidgetItem
from PyQt4 import uic
from os import listdir, path, stat, startfile
from mimetypes import MimeTypes

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("treeWidget.ui", self)
        self.botonBuscar.clicked.connect(self.getDir)
        self.directorio.itemDoubleClicked.connect(self.openElement)
        
    def getDir(self):
        #Eliminar todas las filas de la busqueda anterior
        self.directorio.clear()
        #Ruta indicada por el usuario
        dir = self.ruta.text()
        #Si es un directorio
        if path.isdir(dir):
            #Recorrer sus elementos
            for element in listdir(dir):
                name = element
                pathinfo = dir + "\\" + name
                information = stat(pathinfo)
                #Si es un directorio
                if path.isdir(pathinfo):
                    type = "Carpeta de archivos"
                    size = ""
                else:
                    mime = MimeTypes()
                    type = mime.guess_type(pathinfo)[0]
                    size = str(information.st_size) + " bytes"
                #Fecha de modificacion
                date = str(time.ctime(information.st_mtime))
                #Crear un array para crear la fila con los items
                row = [name, date, type, size]
                #Insertar la fila
                self.directorio.insertTopLevelItems(0, [QTreeWidgetItem(self.directorio, row)])
                
    def openElement(self):
        #Obtener el item seleccionado por el usuario
        item = self.directorio.currentItem()
        #Crear la ruta accediendo al nombre del elemento (carpeta o archivo)
        elemento = self.ruta.text() + "\\" + item.text(0)
        #Si es un directorio -> aceder
        if path.isdir(elemento):
            self.ruta.setText(elemento)
            self.getDir()
        else: #Si es un archivo, abrirlo
            startfile(elemento)
        
            
        
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()