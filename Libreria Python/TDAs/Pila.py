# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 12:46:31 2018

@author: sanch
"""

max = 20

class pila():
    def __init__(self):
        self.tope = -1
        self.est=[]
        for i in range(0,max):
            self.est.append(0)
        
    def pilaLlena(self):
        return self.tope==max-1
    
    def pilaVacia(self):
        return self.tope==-1
        
    def tamañoPila(self):
        return self.tope+1
        
    def apilar(self, x):
        self.tope+=1
        self.est[self.tope]=x
        
    def desapilar(self):
        x=self.est[self.tope]
        self.tope-=1
        return x