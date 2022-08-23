import random
from TDAPilaDin import pila, pilaVacia, tamañoPila, apilar, desapilar


p=pila()
p2=pila()
pPares=pila()
pWord=pila()

def verPila(p):
    pAux = pila()
    for i in range(0, tamañoPila(p)):
        x=desapilar(p)
        print(x)  
        apilar(pAux,x)
    recuperarPila(pAux,p)
                
def cargarPilaRandom(p, n):
    for i in range(0, n):
        x = random.randint(0,25)  
        apilar(p,x)     
        
def cargarElemento(p, x):
    apilar(p,x)
    
def recuperarPila(p2, p):
    while not pilaVacia(p2):
        x=desapilar(p2)
        apilar(p,x)
#1    
def buscarElementos(p, busk): 
    cont = 0
    while not pilaVacia(p):
        x=desapilar(p)
        apilar(p2,x)
        if x == busk:
            cont+=1
    recuperarPila(p2,p)
    return cont
        
#2
def eliminarImpares(p):
    while not pilaVacia(p):
        x = desapilar(p)
        if x % 2 == 0:
            apilar(pPares, x)
    recuperarPila(pPares,p)

#3
def cambiarElemento(p, busk, niu): #cambiar determinado elemento por otro
    ok = -1
    for i in range (0, tamañoPila(p)):
        x = desapilar(p)
        if x == busk:
            ok = busk
            apilar(p2 , niu)
        else:
            apilar(p2,x)
    recuperarPila(p2,p)
    return ok == busk

            
def invertirPila(p):
    pAux = pila()    
    for i in range (0, tamañoPila(p)):
        x = desapilar(p)
        apilar(pAux, x)
    return pAux
    
def palindromo(p):
    pAux=pila()
    cant = tamañoPila(p)
    cont = 0
    for i in range (0, tamañoPila(p)):
        x = desapilar(p)
        apilar(p2, x)
        apilar(pPares, x)
    pAux = invertirPila(pPares)
    for i in range (0, tamañoPila(pAux)):    
        x = desapilar(pAux)
        y = desapilar(p2)
        if x == y:
            cont+=1
        apilar(p,y)
    return cont == cant
    
def cadenaXCY(p):
    return ((tamañoPila(p)%2==1) and palindromo(p))

def verAlReves(p):
    p2=invertirPila(p)
    verPila(p2)
        
def desapilarSubTope(p): #8
    x=desapilar(p)
    desapilar(p)
    apilar(p,x)        
        
def getElementoPila(p,pos):
    pAux = pila()
    for i in range(0, tamañoPila(p)):
        x=desapilar(p)
        if i==pos:
            y=x
        apilar(pAux,x)      
    recuperarPila(pAux,p)
    return y                            


print("1. cargar manualmente la pila")
print("2. cargar la pila automaticamente")   
opc = int(input("ingrese opcion: "))     
while opc!=1 and opc!=2:    
    if opc!=1 and opc!=2:
        print("opcion incorrecta")        
        print()
        print("1. cargar manualmente la pila")
        print("2. cargar la pila automaticamente")
        print()
        opc = int(input("ingrese opcion: "))

n=int(input("¿cuantos elementos desea cargar? (máixmo 10): "))
while n > 10:
    print("error, demasiados elementos")
    n=int(input("¿cuantos elementos desea cargar? (máixmo 10): "))
        
if opc==1:
    for i in range(0, n):
        x = input("ingrese un elemento: ")
        cargarElemento(p,x)
else:
    cargarPilaRandom(p,n)
verPila(p)    
   
busk = int(input("ingrese el elemento que desea buscar en la pila: "))
cant=buscarElementos(p, busk)
if cant == 0:
    print("el elemento no aparece")
elif cant == 1:
    print("el elemento aparece 1 vez")
else:
    print("el elemento buscado aparece ",cant," veces")
    
opc = input("¿Desea eliminar los numeros impares?: si/no ")
while opc != "si" and opc != "no":
    print("opcion incorrecta")
    opc = input("¿Desea eliminar los numeros impares?: si/no ")
if opc == "si":
    eliminarImpares(p)
verPila(p)    
    
busk = int(input("que numero desea reemplazar?: "))
cant=buscarElementos(p, busk)
if cant == 0:
    print("el elemento no aparece")
else:
    x=int(input("por que numero desea reemplazarlo?: "))
    if cambiarElemento(p,busk,x):    
        verPila(p)
print()
print("pila invertida:")
p2=invertirPila(p)
p=p2
verPila(p)  
print()
print("eliminando elemento debajo del tope: ")
desapilarSubTope(p)
verPila(p)
busk=int(input("¿Que posicion de la pila desea conocer?:"))
print("el elemento que usted solicitó es: ",getElementoPila(p,busk-1))
print()

           
word=input("ingrese una palabra: ")
for i in range(0,len(word)):
    cargarElemento(pWord,word[i]) 
verPila(pWord) 
if palindromo(pWord):
    print("la palabra es palindromo")
else:
    print("la palabra no es palindromo") 

if (tamañoPila(pWord)%2==1) and palindromo(pWord):
    print("esta cadena de caracteres es de la forma xCy, donde x es el inverso de y")
#7
print("Al reves")
verAlReves(pWord)

if cadenaXCY(p):
    print("esta cadena de caracteres es de la forma xCy, donde x es el inverso de y")

      
        






 

