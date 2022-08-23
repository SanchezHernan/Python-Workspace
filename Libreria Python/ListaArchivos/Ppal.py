from Lista import lista, regLista, insertarEnLista, eliminarDeLista, lenght, mostrarLista
from Archivos import leer, abrir, cerrar, guardar, regArchivo, modificar
import os
        
l=lista()
ruta = os.path.realpath('ArchivoLista/orden.txt')

def cargarLista(l):
    archivo=abrir(ruta)
    for i in range(0,len(archivo)):
        ra=leer(archivo,i)
        if ra.info!= None:
            if ra.activo:
                rl=regLista()
                rl.info=ra.info
                rl.pos=i
                insertarEnLista(l, rl)
                print(len(archivo)+' elementos cargados')
    cerrar(archivo)
 
def ingresar(l, ruta):
    rl=regLista()
    ra=regArchivo()
    archivo=abrir(ruta)
    ra.info=rl.info=input('ingrese el elemento que desea almacenar: ')
    #ra.info=rl.info
    rl.pos=len(archivo)
    guardar(archivo,ra)
    insertarEnLista(l,rl)
    print('Elemento ingresado correctamente')
    
       
def eliminar(ruta):
    ra=regArchivo()
    var = eliminarDeLista(l,input('ingrese la clave del elemento a eliminar: '))
    if (var == None):
        print('Clave no encontrada')
    else:
        ra.activa=False
        ra.info=var.info
        archivo=abrir(ruta)
        modificar(archivo,ra,var.pos)
        print('Eliminacion completada')
        cerrar(archivo)
        
def modificacion():
    x=eliminarDeLista(l,input('ingrese la clave del elemento que desea buscar para modificar: '))
    if x!= None:
        print('Elemento encontrado')
        x.info=input('ingrese la nueva informacion: ')
        insertarEnLista(l,x)
    else:
        print('Clave no encontrada')
        
def mostrarMenu():
    print("1. Ingresar")
    print("2. Eliminar")
    print("3. Modificar")
    print("4. Listar")
    print("0. Salir")
    return int(input("que opcion desea reaizar?: ")) 
    
def guardarEnArchivo(l, ruta):
    archivo=abrir(ruta)
    ra=regArchivo()
    for i in range(0, lenght(l)):   
        rl=l.eliminarCabecera()
        if rl!= None:
            ra=leer(archivo, rl.pos)
            if ra != None:
                if rl.info!=ra.info:
                    ra.info=rl.info
                    modificar(archivo, ra, rl.pos)
            else:
                ra=rl.info
                guardar(archivo, ra)
    cerrar(archivo)

cargarLista(l)   
opc=mostrarMenu()
while (opc != 0):
    if(opc == 1):
        ingresar(l, ruta)
    elif(opc == 2):
        eliminar(ruta)
    elif(opc == 3):
        modificacion()
        print()
    elif(opc == 4):
        mostrarLista(l)
    elif(opc == 0):
        break
    else:
        print('opcion incorrecta')
    print()
    opc = mostrarMenu()
    
guardarEnArchivo(l, ruta)
'''
*Hacer quickSort iterativo con pilas
*Al semaforo darle tiempos distintos
*Ordenar archivo
*
'''