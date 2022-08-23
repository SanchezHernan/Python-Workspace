import shelve

class regArchivo():
    def __init__(self):
        self.info=None
        self.activa=True

def abrir(ruta):
    return shelve.open(ruta)
    
def cerrar(archivo):
    archivo.close()
    
def guardar(archivo, reg):
    archivo[str(len(archivo))]=reg
    
def modificar(archivo,reg,pos):
    archivo[str(pos)]=reg
    
def leer(archivo,pos):
    return  archivo[str(pos)]





    
