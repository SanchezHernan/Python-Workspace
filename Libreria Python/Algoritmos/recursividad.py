""" libreria de funciones unidad 1: recursividad"""

def factorial(num):   #tambien se comenta asi
    if (num==0):
        return 1
    else:
        return num*factorial(num-1)
    
 
def factoriali(num):
    aux=1
    
    for i in range (num,0,-1): #iterativa
        aux=aux*i
        
    return aux
    
def fibonacci(num):
    if (num==0):
        return 0
    elif (num==1):
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
        
        
def suma(num):   
    if (num==1):
        return 1
    else:
        return num+suma(num-1)
        
def potencia(num1,num2):
    if (num2==0):
        return 1
    
    else:
        return num1*potencia(num1,num2-1)
        
def inversacad(palabra,num):
    if (num==0):
        return palabra[num]   
    else:
        return palabra[num]+inversacad(palabra,num-1)


def inversornum(num,digitos):
    if (digitos==0):
        return num[digitos]
    else:
        return num[digitos]+inversornum(num,digitos-1)
        