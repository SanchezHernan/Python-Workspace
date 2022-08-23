# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:17:40 2018

@author: Hornyt0x
"""

import shelve

def abrir(ruta):
    return shelve.open(ruta)
    
def cerrar(archivo):
    archivo.close()
    
def guardar(archivo, key, reg):
    archivo[key]=reg
    
def modificar(archivo,reg,pos):
    archivo[str(pos)]=reg
    
def leer(archivo,pos):
    return  archivo[str(pos)]