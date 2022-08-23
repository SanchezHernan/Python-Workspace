import sys
from PyQt4.QtGui import QApplication, QMainWindow, QAction, QMessageBox,QIcon
from PyQt4 import uic

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(800,500)
        self.setWindowTitle("Ventanita")
        #Barra de estado
        self.statusBar().showMessage("Bienvenid@")
        #Objeto menuBar
        menu = self.menuBar()
        #Menus padre
        menu_archivo = menu.addMenu("&Archivo")
        menu_editar = menu.addMenu("&Editar")
        
        #Agregar un elemento accion al menu_archivo
        menu_archivo_abrir = QAction(QIcon(), "&Abrir", self)
        menu_archivo_abrir.setShortcut("Ctrl+o")
        menu_archivo_abrir.setStatusTip("Abrir")
        menu_archivo_abrir.triggered.connect(self.menuArchivoAbrir) #Lanzador
        menu_archivo.addAction(menu_archivo_abrir)
        
        #Agregar un elemento accion al menu_archivo
        menu_archivo_cerrar = QAction(QIcon(), "&Cerrar", self)
        menu_archivo_cerrar.setShortcut("Ctrl+c")
        menu_archivo_cerrar.setStatusTip("Cerrar")
        menu_archivo_cerrar.triggered.connect(self.menuArchivoAbrir) #Lanzador
        menu_archivo.addAction(menu_archivo_cerrar)
        
        #Agregar un submenu al menu editar
        menu_editar_opciones = menu_editar.addMenu("&Opciones")
        menu_editar_opciones_buscar = QAction(QIcon(), "&Buscar", self)
        menu_editar_opciones_buscar.setShortcut("Ctrl+f")
        menu_editar_opciones_buscar.setStatusTip("Buscar")
        menu_editar_opciones.triggered.connect(self.menuEditarOpcionesBuscar)
        menu_editar_opciones.addAction(menu_editar_opciones_buscar)
        
    def menuArchivoAbrir(self):
        QMessageBox.information(self, "Abrir", "Accion Abrir", QMessageBox.Discard)
        
    def menuArchivoCerrar(self):
        QMessageBox.information(self, "Cerrar", "Accion Cerrar", QMessageBox.Discard)
        
    def menuEditarOpcionesBuscar(self):
        QMessageBox.information(self, "Buscar", "Accion Buscar", QMessageBox.Discard)
        
    
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()