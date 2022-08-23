import random
from TDAPilaDin import pila, apilar, desapilar, tamañoPila, pilaVacia
from TDAColaDin import cola, tamañoCola, colaLlena, eliminarDeCola, insertarEnCola, colaVacia

q=cola()
def listarCola(q):
    qAux=cola()
    while not colaVacia(q):
       x = eliminarDeCola(q)
       print(x)
       insertarEnCola(qAux,x)        
    while not colaVacia(qAux):
        x = eliminarDeCola(qAux)
        insertarEnCola(q,x)
                
def llenarCola(q,n):
    i = 0
    while not colaLlena(q) and i < n:
        x = random.randint(0,20) 
        insertarEnCola(q,x)
        i+=1

def invertirCola(q):
    p=pila()
    while not colaVacia(q):
        input("hola")
        x=eliminarDeCola(q)
        print("apilando: ",x)
        apilar(p,x)
    for i in range(0,tamañoPila(p)):
        insertarEnCola(q,desapilar(p))
        
def palindromo2(cad):
    p=pila()
    qAux=cola()
    cont=0
    cant=len(cad)
    for i in range(0, cant):
        insertarEnCola(qAux,cad[i])
        apilar(p,cad[i])
    while not pilaVacia(p):
        x=desapilar(p)
        y=eliminarDeCola(qAux)
        if x==y:
            cont+=1
    return cont==cant
    
def pilaACola(p):
    while not pilaVacia(p):
        insertarEnCola(q,desapilar(p))
    return q    

def colaAPila(q):
    p=pila
    while not colaVacia(q):
        apilar(p,eliminarDeCola(q))
    return p
    
def pilaAPila(p):
    pAux=pila()
    p2=pila()
    while not pilaVacia(p):
        apilar(pAux,desapilar(p))
    while not pilaVacia(pAux):
        apilar(p2,desapilar(pAux))
    return p2

def pilaAlReves(p):
    p2=pila()
    while not pilaVacia(p):
        apilar(p2,desapilar(p))
    return p2
  
def oracionSeparada(q):
    cont=0
    q2=cola()
    qAux=cola()
    while not colaVacia(q) and cont < 1:
        x=eliminarDeCola(q)
        if x==":":
            cont = 1
        elif cont < 1:
            insertarEnCola(qAux,x)
    print("primera parte: ")            
    listarCola(qAux)            
    while not colaVacia(q):
        x=eliminarDeCola(q)
        insertarEnCola(q2,x)
    print("segunda parte: ")
    listarCola(q2)    
    print("tamaño cola 1: ", tamañoCola(qAux))
    print("tamaño cola 2: ", tamañoCola(q2))
    if tamañoCola(qAux) < tamañoCola(q2):
        cont=2  
    elif tamañoCola(qAux)==tamañoCola(q2):
        cont = 3
        c=0
        cant=tamañoCola(qAux)
        for i in range(0, tamañoCola(qAux)):
            x=eliminarDeCola(qAux)
            y=eliminarDeCola(q2)
            if x == y:
                c+=1       
        if c == cant:
            cont = 4
    return cont
           
    
    
    
    
cadena=input("ingrese su oracion: ")        
for i in range(0,len(cadena)):
    insertarEnCola(q,cadena[i])
listarCola(q)
if palindromo2(cadena):
    print("Es palindromo")
else: print("no es palindromo")    
print()
    
    
j=oracionSeparada(q)
print()
if j==0:
    print("No aparece ':'")
elif j==1:
    print("la primera parte de la cadena es mas larga")
elif j==2:
    print("la segunda parte de la cardena es mas larga al final")
elif j==3:
    print("son igual de largas")
else:
    print("las 2 partes de la cadena son iguales")


invertirCola(q)
listarCola(q)
