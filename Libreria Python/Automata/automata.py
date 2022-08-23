import re

def caracterValido(character):
    if(re.match("a",character)):
        return True
    elif(re.match("b",character)):
        return True
    else:
        return False

def cadenaIncorrecta(cadena):
    for c in cadena:
        if not caracterValido(c):
            return True
    return False

class Automata:
    def __init__(self, tabla, estado):
        self.tabla = tabla
        self.cadena = ''
        self.estado = estado
        
    def setCadena(self, cadena):
        self.cadena = cadena
        
    def transformarCaracter(self, ch):
        if (ch == 'a'):
            return 0
        else:
            return 1
        
    def transicion(self, ch):
        self.estado = self.tabla[self.estado][ch]
                    
    def cadenaValida(self):
        for character in self.cadena:
            self.transicion(self.transformarCaracter(character))
        if self.estado != 7:
            return False
        else:
            return True
 
