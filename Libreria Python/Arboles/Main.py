from Arbol import *
from Archivo import *
from ArchiArbol import cargarArboles
ruta = ('C:/Users/Hornyt0x/Desktop/Libreria Python/Arboles/Archivos/file')

'''
guardar clientes, vendedores y sus ventas, arbol utilizado para busquedas y reportes
'''

class registro():
    def __init__(self):
        self.ncv = 0
        self.cliente = ''
        self.importe = None
        self.pagado = None
        self.activa = True
        
    def cargarRegistro(self):
        self.ncv = int(input("Numero de comprobante de venta: "))
        self.cliente = input("Nombre del cliente: ")
        self.importe = float(input("Importe: $"))
        pago = input("Pagado (si/no): ")
        if pago=='si': self.pagado = True
        else: self.pagado = False
    
    def verRegistro(self):
        print("Numero comprobante: ", self.ncv)
        print("Cliente: "+ self.cliente)
        print("Importe: ", str(self.importe))
        if self.pagado:
            print("Pagado")
        else:
            print("No pagado")
            

class ventana():
    def __init__(self):
        self.arbolVenta = crear_arbol()
        self.arbolCliente = crear_arbol()
            
    def mostrarMenu(self):
        print("1. Alta cliente")
        print("2. Modificacion cliente")
        print("3. Baja cliente")
        print("4. Consulta")
        print("0. Salir")
        return input("que opcion desea reaizar?: ")
        
    def menuModificacion(self):
        print("1. Modificar por numero de venta")
        print("2. Modificar por nombre cliente")
        print("0. Salir")
        opc = int(input("que opcion desea reaizar?: "))
        if opc==1:
            self.modificacionPorVenta()
        elif opc==2:
            self.modificacionPorNombre()
        else:
            print('Opcion incorrecta')

    def menuBaja(self):
        print("1. Baja por numero de venta")
        print("2. Baja por nombre cliente")
        print("0. Salir")
        opc = int(input("que opcion desea reaizar?: "))
        if opc==1:
            self.bajaPorVenta()
        elif opc==2:
            self.bajaPorNombre()
        else:
            print('Opcion incorrecta')
            
    def mostrarMenuConsulta(self):        
        print('1. Modificar')
        print('2. Salir')
        return(input('Que accion desea realizar?'))
            
    def alta(self):
        file=abrir(ruta)
        reg= registro()
        opc = 's'
        while opc == 's':
            reg.cargarRegistro()
            insertar_arbol(self.arbolVenta, reg.ncv, len(file))
            insertar_arbol(self.arbolCliente, reg.cliente, len(file))
            guardar(file, reg)
            opc=input('desea dar de alta otro cliente? s/n')
        cerrar(file)
    
    def modificacionPorVenta(self):
        buscado=input('Ingrese el numero de comprobante de venta que desea modificar: ')
        self.modificar(busqueda(self.arbolVenta, buscado))
    
    def modificacionPorNombre(self):
        buscado=input('Ingrese el nombre de cliente que desea modificar: ')
        self.modificar(busqueda(self.arbolCliente, buscado))
        
    def modificar(self, pos):
        file=abrir(ruta)
        reg = registro()
        modificar(file, reg.cargarRegistro(), pos)
        cerrar(file)
        
    def bajaPorVenta(self):
        buscado=input('Ingrese el nombre de comprobante de venta que desea modificar: ')
        pos = buzqueda(self.arbolVenta, buscado)       
        if pos!=None:    
            cliente, venta = self.baja(pos)
            eliminar_nodo(self.arbolCliente, cliente)
            eliminar_nodo(self.arbolVenta, venta)
        else:        
            print('no se ha encontrado el cliente buscado')
        
        
    def bajaPorNombre(self):
        buscado=input('Ingrese el nombre de cliente que desea modificar: ')
        if buscado!=None:    
            cliente, venta = self.baja(busqueda(self.arbolCliente, buscado))
            eliminar_nodo(self.arbolCliente, cliente)
            eliminar_nodo(self.arbolVenta, venta)
        else:
            print('no se ha encontrado el cliente buscado')
            
    def baja(self, pos):
        file=abrir(ruta)
        if file.activa:
            file.activa = False
        else:
            print('Registro no encontrado')
        cerrar(file)
        return (file.nombre, file.ncv)
    
    def resetArboles(self):
        self.arbolVenta=crear_arbol()
        self.arbolCliente=crear_arbol()
        cargarArboles(ruta, self.arbolVenta, self.arbolCliente)
        
    def consultaPorNombre(self):
        buscado=input('Ingrese el nombre de cliente por el que desea consultar: ')
        posiciones = busquedaMultiple(self.arbolCliente(), buscado)
        if posiciones != None:
            registros = []
            file=abrir(ruta)
            for pos in posiciones:
                reg = leer(file, pos)
                registros.append(reg)
                reg.verReg(reg)
            for i in range(0, len(registros)):
                print(str(i) + ': ')
                reg.verReg()
                print()
            opc = 0
            while opcionEntre(opc,1,2):    
                opc = self.mostrarMenuConsulta()
        
        
    def consultaPorNCV(self):
        buscado=input('ingrese el numero a buscar: ')
        
        pos = busqueda(self.arbolVenta, int(buscado))
        if pos != None:
            file=abrir(ruta)
            reg = leer(file, pos)
            reg.verRegistro()
            opc = 0
            while opcionEntre(opc,1,2):
                opc = self.mostrarMenuConsulta()
                if opcionEntre(opc,1,2):
                    print('opcion incorrecta')
            if opc == 1:
                self.modificar(pos)
                
    def consulta(self):
        opc = 5
        while opc < 0 and opc > 2:
            print('1. Realizar consulta por nombre')
            print('2. Consulta por NCV')
            print('0. Volver')
            opc = input('ingrese opcion: ')
        if opc == 0:
            self.mostrarMenu()
        elif opc == 1:
            self.consultaPorNombre()
        else:
            self.consultaPorNCV()
    
    def cargarArboles(self):
        archivo=abrir(ruta)
        for i in range(0,len(archivo)):
            x=leer(archivo,i)
            if x.activa:
                insertar_arbol(self.arbolVenta, x.ncv, i)
                insertar_arbol(self.arbolCliente, x.cliente, i)
        cerrar(archivo)
    

def opcionEntre(numero, inicio, fin):
        if numero < inicio and numero > fin:
            return False
        else:
            return True



ventana = ventana()
ventana.cargarArboles()
opc=int(ventana.mostrarMenu())
while opc!=0:
    if opc==1:
        ventana.alta()
    elif opc==2:
        ventana.menuModificacion()
        ventana.resetArboles()
    elif opc==3:
        ventana.menuBaja()
        ventana.resetArboles()
    elif opc==4:
        ventana.consulta()
    opc=int(ventana.mostrarMenu())


    
