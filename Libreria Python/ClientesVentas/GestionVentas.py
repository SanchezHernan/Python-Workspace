# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:18:01 2018

@author: Hornyt0x
"""
import sys

from PyQt4 import QtGui, uic
from Arbol import *
from Archivo import *
ruta="Archivos/Ventas.dat"


class Registro():
    def __init__(self, cliente, importe, pagado):
        self.cliente = cliente
        self.importe = importe
        self.pagado = pagado


class RegistroModif():
    def __init__(self):
        self.ncv = None
        self.cliente = None
        self.importe = None
        self.pagado = None

        
class MenuModif(QtGui.QDialog):
    def __init__(self, reg):
        QtGui.QDialog.__init__(self)
        uic.loadUi("Interfases/MenuModif.ui", self)
        self.btnModificar2.clicked.connect(lambda: self.modificar(reg))
        self.btnCancelar.clicked.connect(self.cerrar)

        
    def modificar(self, reg):
        reply=QtGui.QMessageBox.question(self, 'Modificacion',
            "Desea realizar los cambios?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
        if reply==QtGui.QMessageBox.Yes:
            reg.cliente = self.leCliente2.text()
            reg.importe = self.leImporte2.text()
            reg.pagado = self.checkBox2.isChecked()
            reg.ncv = self.leNcv2.text()
        self.close()
    
    def cerrar(self):
        self.close()
        

class GestionVentas(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("Interfases/table.ui", self)
        self.arbolVentas = crear_arbol()
        self.arbolClientes = crear_arbol()
        self.dict = {}
        self.keys = []
        self.cargarDiccionario()
        self.iniciarTableWidget()
        self.btnAlta.clicked.connect(self.alta)
        self.btnModificar.clicked.connect(self.modificacion)
        self.btnBuscar.clicked.connect(self.busqueda) 
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnActualizar.clicked.connect(self.actualizar)
        self.statusBar()

        
    def cargarDiccionario(self):
        archVentas = abrir(ruta)
        keys = list(archVentas.keys())
        for k in keys:
            self.keys.append(k)
            self.dict[k] = leer(archVentas,k)
            self.insertarEnArboles(self.dict[k].cliente, k)
        cerrar(archVentas)
            
            
    def iniciarTableWidget(self):
        self.tableWidget.setColumnCount(4)
        self.tableWidget.clear()
        self.cargarTable()


    def addItemToTable(self, item, key):
        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row+1)
        self.tableWidget.setItem(row, 0, QtGui.QTableWidgetItem(key))
        self.tableWidget.setItem(row, 1, QtGui.QTableWidgetItem(item.cliente))          
        self.tableWidget.setItem(row, 2, QtGui.QTableWidgetItem('$ ' + item.importe))            
        if item.pagado:
            self.tableWidget.setItem(row, 3, QtGui.QTableWidgetItem('Si'))
        else:
            self.tableWidget.setItem(row, 3, QtGui.QTableWidgetItem('No'))
    
      
    def guardarEnVentas(self):
        archVentas=abrir(ruta)
        for k in self.dict:
            guardar(archVentas, k, self.dict[k])
        cerrar(archVentas)
            

    def alta(self):
        if self.validar():  
            key = self.leNcv.text()
            cliente = self.leCliente.text()
            pagado = self.checkBox.isChecked()
            reg = Registro(cliente, self.leImporte.text(), pagado)
            self.dict[key] = reg
            self.keys.append(key)
            self.insertarEnArboles(cliente, key)
            self.statusBar().showMessage('Alta exitosa')
            self.leNcv.setText('')
            self.leCliente.setText('')
            self.leImporte.setText('')            
            
            
    def validar(self):
        if buscar(self.arbolVentas, self.leNcv.text()) == None:
            return(len(self.leNcv.text())>0 and len(self.leCliente.text())>0 and len(self.leImporte.text())>0)
        else:
            self.statusBar().showMessage('Numero de comprobante ya existente')
            return False
            
            
    def modificacion(self):
        '''text=self.listWidget.currentItem().text()
        '''
        
        f=text.find('| Cliente')
        key=text[8:f-1]
        print(key)
        if key!=None:
            reg = RegistroModif()
            reg.ncv = key
            reg.cliente = self.dict[key].cliente
            reg.importe = self.dict[key].importe
            reg.pagado = self.dict[key].pagado
            menuModif = MenuModif(reg)
            menuModif.leNcv2.setText(key)
            menuModif.leCliente2.setText(reg.cliente)
            menuModif.leImporte2.setText(reg.importe)
            menuModif.checkBox2.setChecked(reg.pagado)
            menuModif.exec_()
            #si cambia el cliente o la clave que se recarguen los arboles.
            if reg.ncv != key:
                eliminarConNumero(self.arbolClientes, self.dict[key].cliente, key)
                eliminar_nodo(self.arbolVentas, key)
                self.insertarEnArboles(reg.cliente, reg.ncv)
                archivo = abrir(ruta)
                try:    
                    del archivo[key]
                except:
                    print('Dicho dato no se encuentra en el archivo')
                cerrar(archivo)
                del self.dict[key]
            elif reg.cliente != self.dict[key].cliente:
                eliminarConNumero(self.arbolClientes, self.dict[key].cliente, key)
                insertarEnArbol(self.arbolClientes, reg.cliente, reg.ncv)
            reg2 = Registro(reg.cliente, reg.importe, reg.pagado)
            self.dict[reg.ncv] = reg2
        else:
            self.statusBar().showMessage('No se ha encontrado Resultado')

            
    def eliminar(self):
        k=self.obtenerKeyDeList()
        preorden(self.arbolVentas)
        reply=QtGui.QMessageBox.question(self, 'Advertencia',
            "Seguro que desea eliminar esta venta?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
        if reply == QtGui.QMessageBox.Yes:    
            if k != None:
                print(k)
                eliminarConNumero(self.arbolClientes, self.dict[k].cliente, k)
                eliminar_nodo(self.arbolVentas, k)
                del self.dict[k]
                archivo = abrir(ruta)
                try:
                    del archivo[k]
                except:
                    print('No se encuentra en archivo')
                cerrar(archivo)
       
        
    def busquedaEnArboles(self):
        k = []
        if self.rbVenta.isChecked():
            k.append(buscar(self.arbolVentas, self.leBusqueda.text()))
        elif self.rbCliente.isChecked():
            for key in self.keys:
                f = self.dict[key].cliente.find(self.leBusqueda.text())
                if f > -1:
                    k.append(key)
        return k

            
    def getItem(self):
        self.dict
        item=('Codigo: '+key+' | Cliente: '+reg.cliente+' | Importe: $'+reg.importe)
        if reg.pagado:
            item += ' | Pagado'
        else:
            item += ' | No Pagado'
        return item
        
       
    def busqueda(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        k=self.busquedaEnArboles()
        self.tableWidget.setSortingEnabled(False)
        for key in k:
            if key != None:
                self.addItemToTable(self.dict[key], key)
        self.tableWidget.setSortingEnabled(True)
       
           
    def insertarEnArboles(self, cliente, codigo):
        insertarEnArbol(self.arbolClientes, cliente, codigo)
        insertarEnArbol(self.arbolVentas, codigo, codigo)
        
        
    def closeEvent(self, event):
        self.guardarEnVentas()
        
        
    def cargarTable(self):
        self.tableWidget.setRowCount(0)
        headers = ("Numero venta", "Nombre", "Importe", "Pagado")
        self.tableWidget.setHorizontalHeaderLabels(headers)
        for k in self.keys:
            self.addItemToTable(self.dict[k], k)
        
        
    def actualizar(self):
        self.tableWidget.clear()
        self.tableWidget.setSortingEnabled(False)
        self.cargarTable()
        self.tableWidget.setSortingEnabled(True)
        
                
      
    '''  
    def obtenerKeyDeList(self):
        text=self.listWidget.currentItem().text()
        f=text.find('| Cliente')
        return text[8:f-1]
    '''            
  
      
app = QtGui.QApplication(sys.argv)
menu = GestionVentas()
menu.show()
app.exec_()


#listado general y por proximidad
#ordenar segun donde pico