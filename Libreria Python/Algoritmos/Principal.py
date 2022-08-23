from TDAArbol import crear_arbol, insertar_arbol, inorden
from Archivos import abrir, guardar

class registro():
    ncv, cliente, importe, pagado, activa = int, str, float, bool, bool
    
reg=registro()
a=crear_arbol()


def cargarRegistro(reg):
    reg.ncv=int(input("Numero de comprobante de venta: "))
    reg.cliente=input("Cliente: ")
    reg.importe=float(input("Importe: "))
    pago=input("Pagado (si/no): ")
    if (pago == "si"): reg.pagado=True
    else: reg.pagado=False
    reg.activa = True
    
def verReg(reg):
    print("Numero comprobante: ",reg.ncv)
    print("Cliente: "+reg.cliente)
    print("Importe: ",reg.importe)
    if reg.pagado:
        print("Pagado")
    else:
        print("No pagado")
        
file=abrir("D:\Archivos\File")
for i in range(0,4):
    cargarRegistro(reg)    
    guardar(file,reg)


#char() le pasas el numero y te devuelve el correspondiente simbolo ASCII
#ord() le pasas el simbomo y te devuelve el correspondiente codigo ASCII