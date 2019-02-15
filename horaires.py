# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 08:39:14 2019

@author: dupouyj
"""


class Horaires:
    def __init__(self, ligne, arret, sens, ferie, heures=[]):
        self.ligne=ligne
        self.arret=arret
        self.ferie=ferie
        self.sens=sens
        self.heures=heures
    
    
        