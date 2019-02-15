# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:31:10 2019

@author: dupouyj
"""


class Arc:
    def __init__(self, arret_dep, arret_arr, temps=None):
        self.arret_dep=arret_dep
        self.arret_arr=arret_arr
        self.temps=temps
        
    def setTemps(self,t):
        self.temps=t
    

    