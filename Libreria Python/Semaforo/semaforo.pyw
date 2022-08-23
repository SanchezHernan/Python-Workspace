# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 21:30:12 2018

@author: Hornyt0x
"""

from Semaforo import semaforo
import time
import sys
from PyQt4 import QtGui, uic
sys.path.append('../')
from TDAs.Colas import *



def contarSegundos(tiempo):
    for i in range(0, tiempo):
        start = time.time()
        print('esperando ' + str(i))
        while(time.time() - start < 1):
            QtGui.qApp.processEvents()
            '''algo'''
        
class modeloSem(QtGui.QDialog):
    def __init__(self):
        super(modeloSem, self).__init__()
        self.esquina = cola()
        self.tiempoRojo = 2
        self.initUI()
        self.parado = True
        self.btnModificar.setEnabled(False)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnIniciar.clicked.connect(self.iniciar)
        self.btnParar.clicked.connect(self.parar)
        
        
    def initUI(self):
        uic.loadUi("esquina.ui", self)


    def cargarSem(self):
        try:
            if (self.les1 and self.les2 and self.les3 and self.les4 and self.lesR) != None and \
               int(self.les1.text()) > 0 and int(self.les2.text()) > 0 and \
               int(self.les3.text()) > 0 and int(self.les4.text()) > 0 and \
               int(self.lesR.text()) > 0:
                   
                sem1 = semaforo(1, int(self.les1.text()))
                sem2 = semaforo(2, int(self.les2.text()))
                sem3 = semaforo(3, int(self.les3.text()))
                sem4 = semaforo(4, int(self.les4.text()))
        
                self.esquina.insertarEnCola(sem1)
                self.esquina.insertarEnCola(sem2)
                self.esquina.insertarEnCola(sem3)
                self.esquina.insertarEnCola(sem4)
                self.tiempoRojo = int(self.lesR.text())
                return True
            else:
                self.lblModificar.setText('Informacion Incorrecta!')
                return False
        except:
            self.lblModificar.setText('Informacion Incorrecta!')
            return False
            
    def funcionando(self):
        while not self.parado:
            self.printSemaforos()
        
    def printSemaforos(self):

        x = self.reinsercion()
        pos = x.getPos()
        if pos == 1:
            self.verde1()
        elif pos == 2:
            self.verde2()
        elif pos == 3:
            self.verde3()
        else:
            self.verde4()
        contarSegundos(x.tiempoVerde)
        self.todoRojo()
        contarSegundos(self.tiempoRojo)
        
            
    def reinsercion(self):
        x = self.esquina.eliminarDeCola()
        self.esquina.insertarEnCola(x)
        return x
        
        
    def todoRojo(self):
        self.red1.setStyleSheet("QFrame { background-color: red }")
        self.green1.setStyleSheet("QFrame { background-color: black }")
        self.red2.setStyleSheet("QFrame { background-color: red }")
        self.green2.setStyleSheet("QFrame { background-color: black }")
        self.red3.setStyleSheet("QFrame { background-color: red }")
        self.green3.setStyleSheet("QFrame { background-color: black }")
        self.red4.setStyleSheet("QFrame { background-color: red }")
        self.green4.setStyleSheet("QFrame { background-color: black }")
    
    def verde1(self):
        self.red1.setStyleSheet("QFrame { background-color: black }")
        self.green1.setStyleSheet("QFrame { background-color: green }")
           
        self.red2.setStyleSheet("QFrame { background-color: red }")
        self.green2.setStyleSheet("QFrame { background-color: black }")
           
        self.red3.setStyleSheet("QFrame { background-color: red }")
        self.green3.setStyleSheet("QFrame { background-color: black }")

        self.red4.setStyleSheet("QFrame { background-color: red }")
        self.green4.setStyleSheet("QFrame { background-color: black }")
    
    def verde2(self):
        self.red1.setStyleSheet("QFrame { background-color: red }")
        self.green1.setStyleSheet("QFrame { background-color: black }")
           
        self.red2.setStyleSheet("QFrame { background-color: black }")
        self.green2.setStyleSheet("QFrame { background-color: green }")
           
        self.red3.setStyleSheet("QFrame { background-color: red }")
        self.green3.setStyleSheet("QFrame { background-color: black }")

        self.red4.setStyleSheet("QFrame { background-color: red }")
        self.green4.setStyleSheet("QFrame { background-color: black }")
        
    def verde3(self):
        self.red1.setStyleSheet("QFrame { background-color: red }")
        self.green1.setStyleSheet("QFrame { background-color: black }")
           
        self.red2.setStyleSheet("QFrame { background-color: red }")
        self.green2.setStyleSheet("QFrame { background-color: black }")
           
        self.red3.setStyleSheet("QFrame { background-color: black }")
        self.green3.setStyleSheet("QFrame { background-color: green }")

        self.red4.setStyleSheet("QFrame { background-color: red }")
        self.green4.setStyleSheet("QFrame { background-color: black }")
        
    def verde4(self):
        self.red1.setStyleSheet("QFrame { background-color: red }")
        self.green1.setStyleSheet("QFrame { background-color: black }")
           
        self.red2.setStyleSheet("QFrame { background-color: red }")
        self.green2.setStyleSheet("QFrame { background-color: black }")
           
        self.red3.setStyleSheet("QFrame { background-color: red }")
        self.green3.setStyleSheet("QFrame { background-color: black }")

        self.red4.setStyleSheet("QFrame { background-color: black }")
        self.green4.setStyleSheet("QFrame { background-color: green }")
        
        
    def modificar(self):
        aux = self.esquina
        try:
            for i in range(0,aux.tamCola()):
                s = aux.eliminarDeCola()
                if s.pos == 1:
                    s.setTiempo(int(self.les1.text()))
                elif s.pos == 2:
                    s.setTiempo(int(self.les2.text()))
                elif s.pos == 3:
                    s.setTiempo(int(self.les3.text()))
                elif s.pos == 4:
                    s.setTiempo(int(self.les4.text()))
                aux.insertarEnCola(s)
            tiempoRojo = int(self.lesR.text())
        except:
            self.lblModificar.setText('No se ha podido realizar la moficicacion')
        self.esquina = aux
        self.tiempoRojo = tiempoRojo
        self.lblModificar.setText('Modificacion realizada con exito')
            
        '''
        self.les1.setText('')
        self.les2.setText('')
        self.les3.setText('')
        self.les4.setText('')
        '''
    
    def parar(self):
        self.parado = True
        self.btnIniciar.setEnabled(True)
        self.btnParar.setEnabled(False)
        self.btnModificar.setEnabled(True)
    
    def iniciar(self):
        
        if self.esquina.colaVacia(): 
            b = self.cargarSem()
        if b:
            self.parado = False
            self.btnIniciar.setEnabled(False)
            self.btnParar.setEnabled(True)
            self.btnModificar.setEnabled(False)
            self.lblModificar.setText('')
            self.funcionando()
        
        

if(__name__=="__main__"):
    
    app = QtGui.QApplication(sys.argv)
    semaf = modeloSem()
    semaf.show()
    #semaf.cargarSem(s)
    app.exec_()    
      

        
#ista implementada sobre archivos, registro con siguiente
        
        
