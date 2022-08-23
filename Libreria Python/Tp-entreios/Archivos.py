# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 22:03:48 2017

@author: Seba
"""

import shelve

class regArchivo():
   def __init__(self, info):
       self.info = info
       self.activo = True
   
   def eliminado(self):
       self.activo = False
       

def abrir(ruta):
    return shelve.open(ruta)

def cerrarArch(archivo):
    archivo.close()

def guardar(archivo, reg):
    archivo[str(len(archivo))] = reg

def modificar(archivo, reg, pos):
    try:
        archivo[str(pos)] = reg
        return True
    except:
        return False

def leer(archivo, pos):
    try:
        return archivo[str(pos)]
    except:
        return None
        


''' 
f = abrir('archivo')
reg = registroVertice()
reg.Ciudad = 'cdelu'
guardar(f,reg)
reg = registroVertice()
reg.Ciudad = 'colon'
guardar(f,reg)
cerrar(f)

f = abrir('archivo')
pos =0

while(pos<len(f)):
    a = leer(f,pos)
    print(a.Ciudad)
    pos +=1

f.close()    
'''