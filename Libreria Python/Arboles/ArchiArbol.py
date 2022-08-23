# qt para entorno grafico
from Arbol import insertar_arbol
from Archivo import abrir, cerrar, leer

def cargarArboles(ruta, av, ac):
    archivo=abrir(ruta)
    for i in range(0,len(archivo)):
        x=leer(archivo,i)
        if x.activa:
            insertar_arbol(av, x.ncv, i)
            insertar_arbol(ac, x.cliente, i)
    cerrar(archivo)