from Arch import abrir, guardar, cerrar, leer
#from Grafo import grafo, altaVertice, listarGrafo, generarArco
import OGrafo as g
import Hervaisen
import Geocoder as gc
from Dijkstra import dijkstra, transformarEnDict


class viaje():
    origen, destino, distancia, importe = "", "", 0, 0




rutaVert="C:/Users/Hornyt0x/Desktop/Libreria Python/Final/Archivos/vertices"
rutaArist="C:/Users/Hornyt0x/Desktop/Libreria Python/Final/Archivos/aristas"

class ventana():
    def __init__(self):
        self.grafo = g.grafo()
        self.cargarGrafo()
        
    def createPath(self, nombre):
        return '%s' % nombre + ' Entre Rios'
    
    def cargarGrafo(self):
        vertices=abrir(rutaVert)
        aristas=abrir(rutaArist)
        for i in range(0,len(vertices)):
            ciudad=leer(vertices,i)
            self.grafo.altaVertice(ciudad)
        cerrar(vertices)
        for i in range(0,len(aristas)):
            viaje=leer(aristas,i)
            self.grafo.generarArco(viaje)
        cerrar(aristas)
    
    
    def cargarCiudad(self):
        ciudad=g.ciudad(input('Ingrese en nombre de la ciudad: '))
        geop = gc.geocoder(ciudad.nombre + ' Entre Rios')
        ciudad.setLatitud(geop['lat'])
        ciudad.setLongitud(geop['lng'])
        self.grafo.altaVertice(ciudad)
              
    def cargarViaje(self):
        viaje = g.viaje()
        viaje.setOrigen(input('Ingrese ciudad de origen: '))
        viaje.setDestino(input('Ingrese ciudad destino: '))
        viaje.setImporte(input('Ingrese importe del viaje: '))
        viaje.setDistancia(Hervaisen.geo_distance(viaje.origen.getLongitud(),
            viaje.origen.getLatitud(),
            viaje.destino.getLongitud(),
            viaje.destino.getLatitud()))
        self.grafo.generarArco(viaje)     
        
    
    def guardarEnArchivo(self):
        archVert = abrir(rutaVert)
        ciudades = self.grafo.getCiudades()
        print(ciudades)
        if ciudades != None:
            for ciudad in ciudades:
                if ciudad.getIdCiudad() == None:
                    ciudad.setIdCiudad(len(archVert))
                    guardar(rutaVert, ciudad)   
        cerrar(archVert)
        archArist = abrir(rutaArist)
        viajes = self.grafo.getViajes()
        if viajes != None:
            for viaje in viajes:
                if viaje.getIdViaje() == None:
                    viaje.setIdViaje(len(archArist))
                    guardar(archArist, viaje)
        cerrar(archArist)
     
    def mostrarMenu(self):
        print("1. Cargar ciudad")
        print("2. Cargar viaje")
        print("3. Listar mapa")
        print("0. Salir")
        return int(input("que opcion desea reaizar?: ")) 
   
    
    
ventana = ventana()
opc = ventana.mostrarMenu()



while (opc != 0):
    if(opc == 1):
        ventana.cargarCiudad()
    elif(opc == 2):
        ventana.cargarViaje()
    elif(opc == 3):
        ventana.grafo.listarGrafo()
        print()
    elif(opc == 4):
        input('')
    elif(opc == 0):
        ventana.guardarEnArchivo()
        i = 10
    opc = ventana.mostrarMenu()
    
        
       
#grapho = transformarEnDict(g)     
       
#dijkstra(grapho, 'Rosario del Tala', 'Concepcion del Uruguay')
        
    
        
    


'''
archivo=abrir(vertices)
guardar(archivo, 'Chajari')
guardar(archivo, 'Concordia')
guardar(archivo, 'Concepcion del Uruguay')
guardar(archivo, 'Diamante')
guardar(archivo, 'Parana')
guardar(archivo, 'Rosario del Tala')
guardar(archivo, 'Victoria')
cerrar(archivo)
'''