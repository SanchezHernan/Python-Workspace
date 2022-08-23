max = 10

class cola():
    def __init__(self):
        self.est=[]
        self.fre = 0
        self.fin = -1
        self.tam = 0
        for i in range(0,max):
            self.est.append(0)
            
q=cola()

def colaLlena(q):
    return q.tam==max
    
def colaVacia(q):
    return q.tam==0
    
def tamañoCola(q):
    return q.tam
    
def insertarEnCola(q, x):
    if q.fin == max-1:
        q.fin = -1
    q.fin+=1
    q.est[q.fin]=x
    q.tam+=1
   
def eliminarDeCola(q):
    x = q.est[q.fre]
    if q.fre == max-1:
        q.fre = -1
    q.fre+=1
    q.tam-=1
    return x
        
def getFrente(q):
    return q.fre
    
    