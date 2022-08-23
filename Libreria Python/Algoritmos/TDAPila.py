max = 10

class pila():
    def __init__(self):
        self.tope = -1
        self.est=[]
        for i in range(0,max):
            self.est.append(0)
        
p=pila()

def pilaLlena(p):
    return p.tope==max-1
    
def pilaVacia(p):
    return p.tope==-1
    
def tamañoPila(p):
    return p.tope+1
    
def apilar(p, x):
    p.tope+=1
    p.est[p.tope]=x
    
def desapilar(p):
    x=p.est[p.tope]
    p.tope-=1
    return x
    
