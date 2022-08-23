
from PyQt4 import QtCore, QtGui, uic

from interfaz.guardar_muestra import guardarMuestra
from interfaz.menu_prestar import prestarMuestra
from entidades.escultura import Escultura
from entidades.pintura import Pintura
from entidades.dinosaurio import Dinosaurio

menu = uic.loadUiType("interfaz/menu_muestra.ui")[0]

def orden_tipo(item):
    return str(type(item))

class Menu_Muestra(QtGui.QDialog, menu):
    
    def __init__(self, museo=None, lista_museos=None, parent=None,):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.museo = museo
        self. combo = QtGui.QComboBox()
        self.lista_museos = lista_museos
        self.actualizar_tabla()
        self.detalle.clicked.connect(self.ver_detalle)
        self.agregar.clicked.connect(self.cargar_muestra)
        self.ordenar.clicked.connect(self.ordnar_muestra)
        self.prestar.clicked.connect(self.prestar_muestra)
        
    def prestar_muestra(self):
        fila = self.tabla.currentRow()
        if (fila>-1):
            self.lista_museos.remove(self.museo)
            dial = prestarMuestra(self.lista_museos)
            dial.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            dial.setModal(True)        
            dial.exec_()
            self.lista_museos.append(self.museo)
            #obtenemos museo destino
            destino = dial.museo
            if(destino != None):
                muestra = self.museo.muestras[fila]
                self.museo.muestras.remove(muestra)
                destino.muestras.append(muestra)
                
        
    
    def ordnar_muestra(self):
        self.museo.muestras.sort(key=orden_tipo)
        self.actualizar_tabla()
    
    def cargar_muestra(self):
        dial = guardarMuestra(self.museo)
        dial.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dial.setModal(True)        
        dial.exec_()
        self.actualizar_tabla()
    
    def ver_detalle(self):
        fila = self.tabla.currentRow()
        if fila>-1:
            muestra = self.museo.muestras[fila]
            if (isinstance(muestra, Pintura)):
                dial = detallePintura(muestra)
                dial.setAttribute(QtCore.Qt.WA_DeleteOnClose)
                dial.setModal(True)        
                dial.exec_()
            elif(isinstance(muestra, Escultura)):
                #abrir detalle escultura
                pass
            elif(isinstance(muestra, Dinosaurio)):
                #abrir detalle dino...
                pass
            
    
    def actualizar_tabla(self):
        self.tabla.setRowCount(0)
        for muestra in self.museo.muestras:
            self.tabla.insertRow(self.tabla.rowCount())
            self.tabla.setItem(self.tabla.rowCount()-1, 0, 
                               QtGui.QTableWidgetItem(str(muestra.codigo)))        
            self.tabla.setItem(self.tabla.rowCount()-1, 1, 
                               QtGui.QTableWidgetItem(muestra.anio_ingreso))
            tipo = ""
            if (isinstance(muestra, Pintura)):
                tipo = "Pintura"
            elif(isinstance(muestra, Escultura)):
                tipo = "Escultura"
            elif(isinstance(muestra, Dinosaurio)):
                tipo = "Dino..."
            self.tabla.setItem(self.tabla.rowCount()-1, 2, 
                               QtGui.QTableWidgetItem(tipo))
    '''

    def cargar_museo(self):
        self.museo = entidades.museo.Museo()
        self.museo.nombre = self.nombre.text()
        self.museo.direccion = self.direccion.text()
        self.hide() 
    ''' 