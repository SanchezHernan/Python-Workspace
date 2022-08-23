class nodoQ():
    info,sig=None,None

class cola():
    def __init__(self):
        self.fre = None
        self.fin = None
        self.tam = 0
        
    def colaVacia(self):
        return self.fre==None
        
    def colaLlena(self):
        return False
        
    def tamCola(self):
        return self.tam
        
    def insertarEnCola(self, x):
        aux = nodoQ()
        aux.info = x
        aux.sig = None
        if self.colaVacia():
            self.fre = aux
        else:
            self.fin.sig = aux
        self.fin = aux
        self.tam += 1
    
    def eliminarDeCola(self):
        x = self.fre.info
        self.fre = self.fre.sig
        if self.colaVacia():
            self.fin = None
        self.tam -= 1
        return x
