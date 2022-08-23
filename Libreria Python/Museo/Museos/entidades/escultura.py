# -*- coding: utf-8 -*-

from entidades.muestra import Muestra

class Escultura(Muestra):
    def __init__(self):
        self.material = None
        self.peso = None
        self.anio = None

