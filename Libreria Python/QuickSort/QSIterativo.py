import sys
sys.path.append('../')
from TDAs.Pila import *

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
           