# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic


menu = uic.loadUiType("interfaz/mapa.ui")[0]
 
class DialogMapa(QtGui.QDialog, menu):
    
    def __init__(self, lista, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.visor.show()
        center ="center=villaguay entre rios"
        zoom = "&zoom=7"
        size = "&size=600x500"
        lista_mapa = ["concepcion del uruguay", "villaguay","parana entre rios"]
        marcas = "|"
        marcas = marcas.join(lista_mapa)
        markers = "&markers=" + "color:green|"+ marcas
        path = "&path=concepcion del uruguay|villaguay"
        imgformat = "&format=png"
        maptype="&maptype=roadmap"
        sensor = "&sensor=false"
        self.visor.load(QtCore.QUrl("https://maps.googleapis.com/maps/api/staticmap?"+center+zoom
                        +size+markers+path+imgformat+maptype+sensor))
        print("https://maps.googleapis.com/maps/api/staticmap?"+center+zoom
                        +size+markers+path+imgformat+maptype+sensor)
        #+size+markers+imgformat+maptype+sensor))
        #self.museo = None
        #self.cargar.clicked.connect(self.cargar_museo)
        
    '''    
    def cargar_museo(self):
        self.museo = Museo()
        self.museo.nombre = self.nombre.text()
        self.museo.direccion = self.direccion.text()
        self.hide() 
        
        "
        markers = "&markers=" + direcciones 
        path = "&path=" + marcas
        "
    '''
