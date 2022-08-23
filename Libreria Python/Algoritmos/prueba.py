import random
vec = []

def cargarListaRandom(vec, tam):
    for i in range(0,tam):
        n = random.randint(0,500)
        vec.append(n) #para cargar un elemento
        return vec
 
def cargarListaManual():
    tam=int(input("Cantidad de numeros a ingresar: "))           
    for i in range(0,tam):
        vec.append(int(input("ingrese numero: ")))
    return vec
    
def listar(vec,tam):
    for i in range(0,tam):
        print(vec[i])
        
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
        

def bBin(vec, busk, izq, der):  #by Hornyx
    med=(izq+der)//2
    if vec[med] == busk:
        return med
    elif vec[med] > busk and med > izq:
        return bBin(vec, busk, izq, med-1)
    elif vec[med] < busk and med < der:
        return bBin(vec, busk, med+1, der)
    if (med == izq or med == der) and vec[med] != busk: 
        return -1
        
        
A=cargarListaManual()
quickSort(A,0,len(A)-1)
listar(A,len(A))  
numero=int(input('ingrese numero: '))
med = bBin(A, numero, 0, len(A)-1)
if (med == -1):
    print("elemento no encontrado")
else:
    print("elemento encontrado en la posicion: ", med)
