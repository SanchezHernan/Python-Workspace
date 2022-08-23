class semaforo():
    def __init__(self, pos, tiempoVerde):
        self.tiempoVerde = tiempoVerde
        self.pos = pos
  
  
    def setTiempo(self, t):
        self.tiempoVerde = t        
    
        
    def getPos(self):
        return self.pos
        
        
    '''
    def cambiarColor(self):
        if self.color == 'verde':
            self.color = 'rojo'
        else:
            self.color = 'verde'
            
    def getColor(self):
        return self.color
    '''   
