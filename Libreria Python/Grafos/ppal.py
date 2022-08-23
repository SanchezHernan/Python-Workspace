from graf import *

g=grafo()
g.altaVertice("A")
g.altaVertice('B')
g.altaVertice("C")
g.altaVertice("D")
g.generarArco('A', 'B')
g.generarArco('A', 'C')
g.generarArco('C', 'D')
g.generarArco('D', 'A')
g.generarArco('A', 'A')
g.listarGrafo()