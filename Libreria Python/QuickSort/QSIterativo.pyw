import sys
sys.path.append('../')
from TDAs.Pila import *
from PyQt4 import QtGui, QtCore
from PyQt4 import uic

vec = []

class Dialogo(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setWindowTitle("Cuadro de dialogo")
        uic.loadUi("QQS.ui", self)   
        self.pushButton.clicked.connect(self.agregar)        
        self.botonOrdenar.clicked.connect(self.ordenar)        
        
    def agregar(self):
        num = int(self.lineEdit.text())
        vec.append(num)
        self.lineEdit.clear()
        if self.label2.text() == '':
            self.label2.setText('Numeros: ' + str(num))
        else:
            nums = self.label2.text()
            nums += ', '+str(num)
            self.label2.setText(nums)
            
        
    def ordenar(self):
        if len(vec) > 0:           
            quickSortIt(vec, 0, len(vec)-1)   
            nums=listar(vec)
            self.label2.setText('Numeros: ' + nums)
        else:
            self.label2.setText('No ha ingresado ningun numero')
        
def quickSortIt(vec, left, right):
    p = pila()
    reg=(left,right)
    p.apilar(reg)
    #Main loop to pop and push items until stack is empty
    while not p.pilaVacia():      
        pos = p.desapilar()
        right, left = pos[1], pos[0]
        pivot = particion(vec,left,right)
        #If items in the left of the pivot push them to the stack
        if pivot-1 > left:
            reg=((left,pivot-1))
            p.apilar(reg)
        #If items in the right of the pivot push them to the stack
        if pivot+1 < right:
            reg=((pivot+1,right))
            p.apilar(reg)


def particion(vec, left, right):
    pivot = vec[left]
    i = left + 1
    j = right
 
    while 1:
        while i <= j  and vec[i] <= pivot:
            i +=1
        while j >= i and vec[j] >= pivot:
            j -=1
        if j <= i:
            break
        #Intercambio entre vec[i] y vec[j]
        vec[i], vec[j] = vec[j], vec[i]
    #Intercambio entre el pivote con vec[j]
    vec[left], vec[j] = vec[j], vec[left]
    return j 

def listar(vec):
    nums = str(vec[0])
    for i in range(1,len(vec)):
        nums += (', '+str(vec[i]))
    return nums
      
app = QtGui.QApplication(sys.argv)
ventana = Dialogo()
ventana.show()
app.exec_()    
quickSortIt(vec, 0, len(vec)-1)
print(listar(vec))
   