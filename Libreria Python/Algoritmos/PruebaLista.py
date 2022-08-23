class reg():
    nom, edad, ec, direc = str, int, str, str

from TDALista import lista, listaVacia, insertarEnLista, eliminarDeLista
from TDALista import tamañoLista, insertarDetras, insertarDelante, contarNodos
from TDALista import borrarVocales, separarEnteros, modificarInfo, listarSuma
from TDALista import intercepcion, concatenarListas, liberarLista, mostrarLista
from TDALista import insertarPorNombre, listarNombres
l=lista()
x=reg()
y=reg()






"""
for i in range(0,n):
    x.nom = input("ingrese nombre: ")
    x.edad = int(input("ingrese edad: "))
    x.ec = input("ingrese estado civil: ")
    x.direc = input("ingrese direccion: ")
    insertarPorNombre(l,x)
"""
x.nom = "carlo"
x.edad = 23
x.ec = "soltero"
x.direc = "alla"
insertarPorNombre(l,x)

x.nom = "jose"
x.edad = 21
x.ec = "casau"
x.direc = "aki"
insertarPorNombre(l,x)

listarNombres(l)
    
    