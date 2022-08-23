# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:51:29 2018

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

def insertarEnArbol(raiz, dato, pos):     
    if raiz.info==None:
        raiz.info = dato
        raiz.nrr = pos          
    elif dato<raiz.info:
        if raiz.izq!=None:
            raiz.izq = insertarEnArbol(raiz.izq, dato, pos)
        else:
            raiz.izq = nodoArbol(dato, pos)
    elif dato>=raiz.info:
        if raiz.der!=None:
            raiz.der = insertarEnArbol(raiz.der, dato, pos)
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

def eliminarConNumero(raiz, clave, numero):
    if raiz!=None:
        if clave<raiz.info:
            raiz.izq = eliminarConNumero(raiz.izq, clave, numero)
        elif clave>raiz.info:
            raiz.der = eliminarConNumero(raiz.der, clave, numero)
        elif raiz.nrr != numero:
            raiz.der = eliminarConNumero(raiz.der, clave, numero)
        else:
            if raiz.izq == None:
                raiz = raiz.der
            elif raiz.der == None:
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info, raiz.nrr = aux.info, aux.nrr
    return raiz            

def buscar(raiz, clave):
    pos = None
    if raiz!=None:
        if clave<raiz.info:
            pos = buscar(raiz.izq, clave)
        elif clave>raiz.info:
            pos = buscar(raiz.der, clave)
        else:
            pos = raiz.nrr
    return pos


def buscarNodo(raiz, clave):
    pos = None
    if raiz!=None:
        if clave<raiz.info:
            pos = buscarNodo(raiz.izq, clave)
        elif clave>raiz.info:
            pos = buscarNodo(raiz.der, clave)
        else:
            pos = raiz
    return pos
   
       
def busquedaMultiple(raiz, clave):
    pos = buscarNodo(raiz, clave)
    result = []
    while pos != None:
        if pos.info == clave:
            result.append(pos.nrr)
            pos=pos.der
        elif pos.info>clave:
            pos=pos.izq
        else:
            pos=pos.der
    return result
            
        
def inorden(raiz):
    if raiz!=None:
        inorden(raiz.izq)
        print (raiz.info)
        inorden(raiz.der)
                
def preorden(raiz):
    if raiz!=None:
        print (raiz.info)
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
    

if(__name__ =='__main__'):
    ac = crear_arbol()
    av = crear_arbol()
    k=[]
    insertarEnArbol(ac, 'Flor', '1')
    insertarEnArbol(av, '1', '1')
    insertarEnArbol(ac, 'Vicky', '2')
    insertarEnArbol(av, '2', '2')
    insertarEnArbol(ac, 'Andrea', '3')
    insertarEnArbol(ac, 'Flor', '4')
    insertarEnArbol(ac, 'Flor', '6')
    insertarEnArbol(ac, 'Andrea', '62')
    eliminarConNumero(ac, 'Vciky', '2')
    eliminar_nodo(av, '2')
    k.append(buscar(av, '2'))
    print(k)
        
    