# -*- coding: utf-8 -*-

from entidades.muestra import Muestra

class Pintura(Muestra):
    
    def __init__(self):
        Muestra.__init__(self)
        self.material = None
        self.tecnica = None
        self.anio = None
        self.replica = None
