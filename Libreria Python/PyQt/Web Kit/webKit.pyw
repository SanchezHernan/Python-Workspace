import sys
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtCore import QUrl
from PyQt4 import uic

class Navegador(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("webKit.ui", self)
        #url por defecto
        default_url = "http://google.com"
        self.navegador.setUrl(QUrl(default_url))
        #Agregar al buscador la url por defecto
        self.url.setText(default_url)
        #Desactivar boton back hasta que no haya historial
        self.btnBack.setEnabled(False)
        #Retroceder a la pagina anterior
        self.btnBack.clicked.connect(self.navegador.back)
        self.url.returnPressed.connect(self.navegar)
        self.navegador.urlChanged.connect(self.url_changed)
        
    def navegar(self):
        url = QUrl(self.url.text())
        self.navegador.setUrl(url)
        
    def url_changed(self):
        #Crear un objeto de la pagina para acceder al historial
        page = self.navegador.page()
        history = page.history()
        #Si hay historial activar el boton back
        if history.canGoBack():
            self.btnBack.setEnabled(True)
        else:
            self.btnBack.setEnabled(False)
        #Agregar el cambio de url al campo de busqueda
        url = self.navegador.url()
        self.url.setText(url.toString())
        
app = QApplication(sys.argv)
navegador = Navegador()
navegador.show()
app.exec_()