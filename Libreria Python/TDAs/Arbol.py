# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:18:48 2018

@author: Hornyt0x
"""

class nodoArbol():
    def __init__(self, info=None, nrr=None, izq=None, der=None):
        self.izq=izq
        self.der=der
        self.info=info
        self.nrr=nrr

def crear_arbol():
    return nodoArbol()

def insertar_arbol(raiz, dato, pos):     
    if raiz.info==None:
        raiz.info = dato
        raiz.nrr = pos          
    elif dato<raiz.info:
        if raiz.izq!=None:
            raiz.izq = insertar_arbol(raiz.izq, dato, pos)
        else:
            raiz.izq = nodoArbol(dato, pos)
    elif dato>=raiz.info:
        if raiz.der!=None:
            raiz.der = insertar_arbol(raiz.der, dato, pos)
        else:
            raiz.der = nodoArbol(dato, pos)
    return raiz 

def arbolvacio(raiz):
    return raiz.info == None

def remplazar(raiz):
    aux = None
    if raiz.der==None:
        aux = raiz
        raiz = None
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux

def eliminar_nodo(raiz, clave):
    x = None
    if raiz!=None:
        if clave<raiz.info:
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif clave>raiz.info:
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info            
            if raiz.izq == None:
                raiz = raiz.der
            elif raiz.der == None:
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info, raiz.nrr = aux.info, aux.nrr
    return raiz, x

def busqueda(raiz, clave):
    pos = None
    if raiz!=None:
        if raiz.info == clave:
            pos = raiz
        elif clave < raiz.info:
            pos = busqueda(raiz.izq, clave)
        else:
            pos = busqueda(raiz.der, clave)
    return pos.nrr
   
   
def busquedaPorPosicion(raiz, pos):
    posic = None
    if raiz!=None and raiz.nrr != pos:
        posic = busquedaPorPosicion(raiz.izq)
        busquedaPorPosicion(raiz.der)
        return posic
                        
        
def busquedaMultiple(raiz, clave):
    resultados = []
    nodo = busqueda(raiz, clave)
    if nodo != None:
        while nodo.info == clave:
            resultados.append[nodo]
            nodo = nodo.der
        return resultados
    else:
        return None

        
def inorden(raiz):
    if raiz!=None:
        inorden(raiz.izq)
        print (raiz.info)
        inorden(raiz.der)
                
def preorden(raiz):
    if raiz!=None:
        print (raiz.info.reg.cliente)
        preorden(raiz.izq)
        preorden(raiz.der)

def postorden(raiz):
    if raiz!=None:
        postorden(raiz.der)
        print (raiz.info)        
        postorden(raiz.izq)
        
def  hijoDer(raiz):
    if raiz!=None:
        return raiz.der

def hijoIzq(raiz):
    if raiz!=None:
        return raiz.izq
        
def elementoMinimo(raiz):
    min=raiz.info
    if raiz!=None:
        if raiz.izq != None:
            if raiz.izq.info < min:
                min=elementoMinimo(raiz.izq)
    return min
    
def elementoMaximo(raiz):
    max=raiz.info
    if raiz!=None:
        if raiz.der!=None:
            if raiz.info < max:
                max=elementoMaximo(raiz.der)
    return max