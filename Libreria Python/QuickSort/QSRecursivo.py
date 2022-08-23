# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 12:49:56 2018

@author: sanch
"""

def quickSort(vec, first, last):
    if first<last:    
        pivote = vec[first]
        i = first+1
        j = last
       
        while i < j:
            while vec[i] < pivote and i < last:
                i+=1        
            while vec[j] > pivote and j > i:    
                j-=1 
            if i < j:   #intercambio
                aux = vec[i]
                vec[i] = vec[j]
                vec[j] = aux
                i+=1
                j-=1              
        if vec[j] < pivote:     #posicionamiento de pivote
            aux = vec[j]
            vec[j] = pivote
            vec[first] = aux
            if i == j:      #condicional de incremento de i
                i+=1
        quickSort(vec, first, j-1)
        quickSort(vec, i, last) 
    
def listar(vec):
    nums = str(vec[0])
    for i in range(1,len(vec)):
        nums += (', '+str(vec[i]))
    return nums